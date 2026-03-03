from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def home():
    return FileResponse("index.html")

@app.get("/greet/{name}")
def greet(name: str):
    return {"greeting": f"Hello {name}, welcome to Kubernetes!"}