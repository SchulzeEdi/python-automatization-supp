from langchain.memory import ConversationBufferMemory
from chat.memories.histories.sql_history import InMemoryMessageHistory

def build_memory(chat_args):
    return ConversationBufferMemory(
        chat_memory=InMemoryMessageHistory(
            conversation_id=chat_args.conversation_id
        ),
        return_messages=True,
        memory_key="chat_history",
        output_key="answer"
    )
