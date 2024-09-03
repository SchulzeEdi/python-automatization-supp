from langchain.chat_models import ChatVertexAI
from chat.models import ChatArgs
from llms.chatvertexai import build_llm
from functools import partial
from memories.sql_memory import build_memory
from functools import partial
from vector_stores.pinecone import build_retriever
from chains.retrieval import StreamingConversationalRetrievalChain

retriever_map = {
  "pinecone_3": partial(build_retriever, k=3)
}
memory_map = {
  "sql_buffer_memory": build_memory,
}
llm_map = {
  "vertexai": partial(build_llm, model_name="gemini-1.0-pro")
}

def build_chat():
  retriever = retriever_map['pinecone_3']()
  llm = llm_map["vertexai"]()
  memory = memory_map['sql_buffer_memory']()
  condense_question_llm = ChatVertexAI(streaming=False)

  return StreamingConversationalRetrievalChain.from_llm(
    llm=llm,
    condense_question_llm=condense_question_llm,
    memory=memory,
    retriever=retriever
  )
