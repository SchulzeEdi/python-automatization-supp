from langchain.chat_models import ChatVertexAI
from chat.llms.chatvertexai import build_llm
from functools import partial
from chat.memories.sql_memory import build_memory
from chat.vector_stores.pinecone import build_retriever
from chains.retrieval import StreamingConversationalRetrievalChain

retriever_map = {
  "pinecone_3": partial(build_retriever, k=3)
}
memory_map = {
  "sql_buffer_memory": build_memory,
}
llm_map = {
  "vertexai": partial(build_llm, model_name="textembedding-gecko@001")
}

def build_chat():
  retriever = retriever_map['pinecone_3']()
  llm = llm_map["vertexai"]()
  memory = memory_map['sql_buffer_memory']()
  condense_question_llm = ChatVertexAI(streaming=False)
  try:
    return StreamingConversationalRetrievalChain.from_llm(
      llm=llm,
      condense_question_llm=condense_question_llm,
      memory=memory,
      retriever=retriever
    )
  except Exception as e:
    print(f"Erro ao criar a cadeia de recuperação: {e}")
    raise
