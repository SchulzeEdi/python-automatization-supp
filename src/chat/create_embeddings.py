from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from vector_stores.pinecone import vector_store

def create_embeddings_for_pdf():
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    loader = PyPDFLoader('src/pdf/RegrasMeuCrediárioLight.pdf')
    docs = loader.load_and_split(text_splitter)

    for doc in docs:
        doc.metadata = {
            "page": doc.metadata["page"],
            "text": doc.page_content,
        }

    vector_store.add_documents(docs)
