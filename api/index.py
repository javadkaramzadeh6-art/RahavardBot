from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
def home():
    return {
        "status": "ok",
        "message": "Rahavard Bot API is online!"
    }
