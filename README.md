# python-getting-started
my go to guide to setting up a python project and include a barebone openai execution

## Activating a Virtual Environment in Windows

python -m venv .venv
```.venc\Scripts\activate```

## Install dependencies
```pip install openai```

## Write to requirements.txt file
```pip freeze > requirements.txt```

## Run Docker ollama image with GPUs
```docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama```

## If ollama image is not found, explicity download the image
# Check is image is available
```docker exec -it ollama ollama list```
# Explicitly download the image
```docker exec -it ollama ollama pull gemma4:latest