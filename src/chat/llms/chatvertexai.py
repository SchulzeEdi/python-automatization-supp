from langchain.chat_models import ChatVertexAI

def build_llm(model_name):
    return ChatVertexAI(
        streaming=False,
        model_name=model_name
    )
