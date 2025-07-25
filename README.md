# Gemini Agentic AI Agent

Using Google Gemini API to create an LLM-powered code agent. The LLM is a command-line program capable of reading, updating, and running Python code using the Gemini API.

## Requirements

- Python 3.12 or higher
- Google Gemini API key

## Installation

1) Clone this repository and navigate to the project directory
```bash
  git clone https://github.com/code-qtzl/ai-agent.git
```

2) Install dependencies using uv (recommended) or pip:
```bash
  # Using uv
  uv sync

  # Or using pip
  pip install google-genai python-dotenv
```

## How to use

1) Add a .env file in the root and specify your gemini api key

```
GEMINI_API_KEY="<YOUR_TOKEN_HERE>"
```

2) Run the AI agent with a prompt:
```bash
  python main.py "your prompt here"
```

3) Use the `--verbose` flag to see detailed execution information:
```bash
  python main.py "your prompt here" --verbose
```

> [!WARNING]
> This project is a toy and is for educational purposes only. 

