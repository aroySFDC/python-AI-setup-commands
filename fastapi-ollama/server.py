from fastapi import FastAPI, HTTPException, Body
from ollama import Client as OllamaClient

app = FastAPI()
client = OllamaClient(
    host="http://localhost:11434"
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/chat")
def chat(message: str = Body(..., description="The message")):
    print(f"Received message: {message}")
    try:
        response = client.chat(
            model="gemma4:latest",
            messages=[
                {"role": "user", "content": message}
            ]
        )
        return {"response": response.message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))