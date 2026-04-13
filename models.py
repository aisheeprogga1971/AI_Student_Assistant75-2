from pydantic import BaseModel
from fastapi import FastAPI

class User(BaseModel):
    username: str
    password: str

class Writing(BaseModel):
    text: str


class Question(BaseModel):
    text: str
app = FastAPI()
@app.post("/ask")
def ask(q: Question):
    print("Received:", q.text)
    return {"answer": "OK backend working"}
