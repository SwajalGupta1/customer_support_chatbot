#  Customer Support Chatbot (RAG + ChromaDB + Groq LLaMA + Streamlit)

This project implements an **AI-powered customer support chatbot** using a Retrieval-Augmented Generation (RAG) pipeline. It embeds FAQ data, stores vectors in ChromaDB, retrieves the most relevant answers using semantic search, and generates grounded responses using **Groq’s LLaMA models**. The system is deployed with Streamlit for an intuitive user experience.

---

##  Features

- RAG-based question answering using custom Flipkart-style FAQ data  
- Sentence-transformer embeddings for high-quality semantic understanding  
- Vector search powered by **ChromaDB**  
- Context-grounded responses generated via **Groq LLaMA 3.3–70B Versatile**  
- Streamlit UI for interactive customer support  
- Prebuilt ChromaDB included for faster deployment  
- Clean modular folder structure  

---

##  Tech Stack

- **Python 3.13**  
- **Streamlit**  
- **ChromaDB**  
- **Sentence Transformers**  
- **Groq API (LLaMA)**  
- **dotenv**  
- **FAISS (optional upgrade)**  

---

##  Project Structure

customer_support_chatbot/
│
├── backend/
│ ├── init.py
│ └── rag_pipeline.py
│
├── frontend/
│ ├── init.py
│ └── streamlit_app.py
│
├── embeddings/
│ ├── chroma/ # Prebuilt vector DB
│ └── create_embeddings.py
│
├── data/
│ └── flipkart_faq.csv
│
├── scripts/
│ └── check_dataset.py
│
├── requirements.txt
└── .gitignore







