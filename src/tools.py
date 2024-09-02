from pydantic import BaseModel, Field
from crewai_tools import Tool
import PyPDF2
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from pydantic.dataclasses import dataclass

@dataclass
class PDFVectorStoreTool(Tool, BaseModel):
    pdf_path: str = Field(..., description="Caminho para o arquivo PDF")
    vector_store: FAISS = None

    class Config:
        arbitrary_types_allowed = True

    def __post_init__(self):
        self.vector_store = self.create_vector_store()

    def extract_text_from_pdf(self):
        with open(self.pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text()
        return text

    def create_embeddings(self, text):
        embeddings = OpenAIEmbeddings()
        texts = [text[i:i+1000] for i in range(0, len(text), 1000)]
        return texts, embeddings.embed_documents(texts)

    def create_vector_store(self):
        text = self.extract_text_from_pdf()
        texts, embeddings = self.create_embeddings(text)
        vector_store = FAISS.from_texts(texts, OpenAIEmbeddings())
        return vector_store

    def run(self, query):
        llm = OpenAI(temperature=0)
        qa_chain = load_qa_chain(llm, chain_type="stuff")
        results = self.vector_store.similarity_search(query, k=3)
        return qa_chain.run(input_documents=results, question=query)
