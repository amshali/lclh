from abc import abstractmethod
from langchain_core.messages import AIMessage, HumanMessage

from langchain_openai import ChatOpenAI
from prompts import chat_openai_prompt


class LlmAdapter:
    def __init__(self, name: str):
        self.name = name
        pass

    @abstractmethod
    def process_input(self, input: str) -> str:
        return ""

    def __str__(self):
        return f"{self.name}"


class ChatOpenAILlmAdapter(LlmAdapter):
    def __init__(self, llm: ChatOpenAI):
        super().__init__("ChatOpenAI")
        self.chain = chat_openai_prompt | llm
        self.history = []

    def process_input(self, input: str) -> str:
        response = self.chain.invoke(
            {"input": input, "chat_history": self.history}
        ).content
        self.history.append(HumanMessage(content=input))
        self.history.append(AIMessage(content=response))
        return response
