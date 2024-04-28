# Linux Command Line Helper (lclh)

This is a Python-based command line tool that helps users generate Linux commands based on their needs. It uses an AI model to generate the commands.

## Installation

1. Clone this repository:

```bash
git clone https://github.com/amshali/lclh.git
cd lclh
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Usage

Run the program with:

```bash
python lclh.py --env-path /path/to/config/.env
```

3. Build and publish binary package

```bash
pyinstaller --onefile lclh.py && sudo cp dist/lclh /usr/local/bin/
```

When prompted, describe what you need to do in Linux. The program will generate a list of commands that can accomplish your task.

## Contributing

Please submit issues and pull requests on the GitHub page for this project.

## License

This project is licensed under the MIT License.
