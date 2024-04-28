from langchain.prompts import PromptTemplate

command_help_prompt = PromptTemplate(
    template="""
Return a bullet list of one-liner linux/unix command(s) for the following task/need.
(Only return the commands, no explanation needed.)

If the input is not something related to linux commands, say "Cannot help with that."

TASK: {input}""",
    input_variables=["input"],
)
