import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
import os
from dotenv import load_dotenv
import requests
from groq import Groq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
groq_client = Groq(api_key=GROQ_API_KEY)

CHROMA_PATH="embeddings/chroma"
COLLECTION_NAME="faq_collection"

embedder = SentenceTransformer('all-MiniLM-L6-v2')

client = chromadb.PersistentClient(path=CHROMA_PATH)
collection=client.get_collection(name=COLLECTION_NAME)

#Search Function

def search_similar(query, top_k=5):
    query_embedding = embedder.encode(query).tolist()
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    matched_docs = []
    for i in range(len(results["documents"][0])):
        matched_docs.append({
            'question': results['documents'][0][i],
            'answer': results['metadatas'][0][i]['answer'],
            'category': results['metadatas'][0][i]['category'],
        })
    return matched_docs

# Build Prompt

def build_prompt(query, retrieved_docs):
    context=""
    for i,doc in enumerate(retrieved_docs):
        context+=f"Q{i+1}: {doc['question']}\nA{i+1}: {doc['answer']}\n\n"
    prompt=f"""
You are a helpful, accurate customer support assitant.
Use ONLY the following context to answer the user's question.
If the answer is not found in the context, say:
"I am sorry, I do not have the enough information regarding that. Please contact customer support for further assistance."

Keep the answer short, clear, and in List/Paragraph format based on the question.

=== CONTEXT ===

{context}

=== USER QUESTION ===

{query}

Provide the best possible answer:
"""
    return prompt.strip()

# LLM Caller

def call_llm(prompt):
    if not GROQ_API_KEY:
        return "❌ GROQ_API_KEY is missing in .env"

    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",   # UPDATED MODEL
        messages=[
            {"role": "system", "content": "You are a helpful support assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.1
    )

    return response.choices[0].message.content


# RAG Pipeline

def answer_question(user_query):
    retrieved = search_similar(user_query, top_k=5)
    prompt = build_prompt(user_query, retrieved)
    answer = call_llm(prompt)
    answer+= "\n\n📞 For more help, contact customer care at **1800-123-4567**."

    return {
        'answer': answer,
        'sources': retrieved
    }

