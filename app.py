from fastapi import FastAPI
from chatbot import get_chatbot

app = FastAPI()
qa = get_chatbot()

@app.get("/chat")
def chat(query: str):
    result = qa.run(query)
    return {"answer": result}

