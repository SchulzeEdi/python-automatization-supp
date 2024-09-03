from langchain.chat_models import ChatVertexAI

def build_llm(chat_args, model_name):
    return ChatVertexAI(
        streaming=chat_args.streaming,
        model_name=model_name
    )
