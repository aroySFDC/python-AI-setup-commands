# python-getting-started
my go to guide to setting up a python project and include a barebone openai execution

## Activating a Virtual Environment in Windows

```python -m venv .venv```
```.venv\Scripts\activate```

## Install dependencies
```pip install openai```

## Write to requirements.txt file
```pip freeze > requirements.txt```

## Run Docker ollama image with GPUs
```docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama```

If ollama image is not found, explicity download the image
## Check if image is available
```docker exec -it ollama ollama list```
## Explicitly download the image
```docker exec -it ollama ollama pull gemma4:latest```

## Run Claude CLI with local model running on docker #
Have qwen3.6 model downloaded and up and running on ollama
Install Claude Code via terminal:
Mac/Linux/WSL: ```curl -fsSL https://claude.ai/install.sh | bash.```
Windows (PowerShell): ```irm https://claude.ai/install.ps1 | iex```
execute claude in your desired directory
```ollama launch claude --model qwen3.6:latest```