import argparse
from dotenv import load_dotenv
import readline
from langchain_openai import ChatOpenAI
import os
from termcolor import colored
import atexit
import sys
import signal
from prompt import command_help_prompt


def exit_handler(signal, frame):
    # Save the readline history before exiting
    readline.write_history_file(history_file)
    sys.exit(0)


# Register the exit handler for the SIGINT signal (usually sent by pressing Ctrl+C)
signal.signal(signal.SIGINT, exit_handler)


def main():
    llm = ChatOpenAI(model=os.getenv("MODEL_NAME"), temperature=0.1)

    chain = command_help_prompt | llm

    readline.parse_and_bind("tab: complete")
    need = input(colored("Describe what you need to do: ", "cyan", attrs=["bold"]))
    result = chain.invoke({"input": need}).content

    # Add the input to the readline history
    readline.add_history(need)
    return result


# Save the readline history when the program exits
atexit.register(readline.write_history_file, "history.txt")


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

    # Parse the command-line arguments
    args = parser.parse_args()
    # Load environment variables from .env file
    load_dotenv(dotenv_path=args.env_path)

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

    result = main()
    # Print command to terminal
    print(f"{result}")
