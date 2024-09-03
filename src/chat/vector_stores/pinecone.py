import os
import pinecone
from langchain_community.vectorstores import Pinecone
from chat.embeddings.vertexai import embeddings

# Inicialização do Pinecone
pinecone.init(
    api_key=os.getenv("PINECONE_API_KEY"),
    environment="us-east-1"
)

# Conectando ao índice existente do Pinecone
vector_store = Pinecone.from_existing_index(
    os.getenv("PINECONE_INDEX_NAME"), embeddings
)

def build_retriever(k):
    search_kwargs = {
        "k": k
    }
    return vector_store.as_retriever(
        search_kwargs=search_kwargs
    )
