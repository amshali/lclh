# Linux Command Line Helper (lclh)

This is a Python-based command line tool that helps users generate Linux commands based on their needs. It uses an _AI model_ to generate the commands.

## Development

1. Clone this repository:

```bash
git clone https://github.com/amshali/lclh.git
cd lclh
```

2. Install the required Python packages:

```sh
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

## Usage

1. Run the program locally with:

```sh
python lclh.py --env-path /path/to/config/.env
```

## Build and Publish

1. Build and publish binary package

```sh
pyinstaller --onefile lclh.py && sudo cp dist/lclh /usr/local/bin/
```

2. Setup your `.env` file

```sh
mkdir -p $HOME/.config/lclh/

echo "OPENAI_API_KEY=?????" >> $HOME/.config/lclh/.env
echo "MODEL_NAME=?????" >> $HOME/.config/lclh/.env

```

3. Add key binding to zsh or bash

For zsh add these to your `.zshrc` file:

```zsh
alias lclh="/usr/local/bin/lclh"

bindkey -s '^u' 'lclh\n'
```

I have chosen `Ctrl+U` as my shortcut key for this. Change it according to your preference.

4. Use it!

Open a new terminal and press `Ctrl+U`. When prompted, describe what you need to do in Linux.
The program will generate a list of commands that can accomplish your task.

## Contributing

Please submit issues and pull requests on the GitHub page for this project.

## License

This project is licensed under the MIT License.
