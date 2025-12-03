import pandas as pd
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
import os

DATA_PATH="data/flipkart_faq.csv"
CHROMA_PATH="embeddings/chroma"

def create_embeddings():

    print("Loading dataset...")
    df=pd.read_csv(DATA_PATH)
    print("Loading embedding model...")
    model=SentenceTransformer('all-MiniLM-L6-v2')
    client=chromadb.PersistentClient(path=CHROMA_PATH)

    collection=client.get_or_create_collection(name="faq_collection",metadata={"hnsw:space":"cosine"})

    print("Creating embeddings and adding to ChromaDB...")

    for idx,row in df.iterrows():
        question=row["question"]
        answer=row["answer"]
        category=row["category"]

        embedding=model.encode(question).tolist()

        collection.add(
            ids=[f"faq_{idx}"],
            embeddings=[embedding],
            documents=[question],
            metadatas=[{"answer": answer, "category": category}]
        )

        if(idx%5==0):
            print(f"Processed {idx} entries...")

    print("Embedding creation completed.")

create_embeddings()