import argparse
from dotenv import load_dotenv
import readline
from langchain_openai import ChatOpenAI
import os
from termcolor import colored
import atexit
import sys
import signal
from lclh_llm import ChatOpenAILlmAdapter, LlmAdapter


def exit_handler(signal, frame):
    # Save the readline history before exiting
    readline.write_history_file(history_file)
    sys.exit(0)


# Register the exit handler for the SIGINT signal (usually sent by pressing Ctrl+C)
signal.signal(signal.SIGINT, exit_handler)


def main(llm_adapter: LlmAdapter):
    print(
        colored(
            "Describe what you need to do(or press enter to exit).",
            "cyan",
            attrs=["bold"],
        )
    )
    while True:
        need = input("> ")
        # If the user presses enter without typing anything, exit the loop
        if need == "":
            break

        result = llm_adapter.process_input(need)

        # Add the input to the readline history if it's not the same as the last input
        if (
            readline.get_current_history_length() == 0
            or need != readline.get_history_item(readline.get_current_history_length())
        ):
            readline.add_history(need)
        print(result)
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Assistant")
    # Add arguments
    default_env_path = os.path.join(os.path.expanduser("~"), ".config/lclh/.env")
    parser.add_argument(
        "--env-path",
        type=str,
        default=default_env_path,
        help="The path to the .env file",
    )

    parser.add_argument(
        "--model",
        type=str,
        choices=["gpt", "llama3"],
        default="gpt",
        help="The model to use (gpt or llama3)",
    )

    # Parse the command-line arguments
    args = parser.parse_args()
    # Load environment variables from .env file
    load_dotenv(dotenv_path=args.env_path)

    llm_adapter = None
    if args.model == "gpt":
        llm_adapter = ChatOpenAILlmAdapter(
            ChatOpenAI(model=os.getenv("MODEL_NAME"), temperature=0.1)
        )

    # Construct the path to the history file
    history_file = os.path.join(os.path.expanduser("~"), ".config/lclh/history")
    # Save the readline history when the program exits
    atexit.register(readline.write_history_file, history_file)

    # Create the directory for the history file if it doesn't exist
    os.makedirs(os.path.dirname(history_file), exist_ok=True)

    # Load the readline history
    try:
        readline.read_history_file(history_file)
    except FileNotFoundError:
        pass

    main(llm_adapter)
