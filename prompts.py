from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_openai_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
Return a bullet list of one-liner linux/unix command(s)
or coding/programming related commands for the following task/need.
(Only return the commands, no explanation needed.)

If the input is not something related to linux commands, say "Cannot help with that."
""",
        ),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)
