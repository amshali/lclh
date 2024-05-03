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


class OllamaLlmAdapter(LlmAdapter):
    def __init__(self, llm, model_name):
        super().__init__("Ollama")
        self.llm = llm
        self.model_name = model_name
        self.history = [
            {
                "role": "system",
                "content": """
Return a bullet list of one-liner linux/unix command(s)
or coding/programming related commands for the following user's task/need.
(Only return the commands, no explanation needed.)

If the user's input is not something related to linux commands, say "Cannot help with that."
        """,
            },
        ]

    def process_input(self, input: str) -> str:
        self.history.append(
            {
                "role": "user",
                "content": input,
            }
        )

        response = self.llm.chat(
            model=self.model_name,
            messages=self.history,
            stream=False,
        )
        self.history.append(response["message"])
        return response["message"]["content"]
