from pydantic import BaseModel
from langchain.schema import BaseChatMessageHistory, BaseMessage

class InMemoryMessageHistory(BaseChatMessageHistory, BaseModel):
    conversation_id: str
    _messages: list[BaseMessage] = []

    @property
    def messages(self):
        return self._messages
    
    def add_message(self, message: BaseMessage):
        self._messages.append(message)

    def clear(self):
        self._messages.clear()
