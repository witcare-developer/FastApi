from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {
        "name" : "Renato Oliveira",
        "age" : 48,
        "email" : "renato@renato.com"
    }