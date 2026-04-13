from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from database import users_collection

app = FastAPI()

# CORS (safe)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    username: str
    password: str

class Question(BaseModel):
    text: str


@app.get("/")
def home():
    return {"message": "Backend running"}


@app.post("/register")
def register(user: User):
    try:
        existing = users_collection.find_one({"username": user.username})

        if existing:
            return {"message": "User already exists"}

        users_collection.insert_one(user.model_dump())  

        return {"message": "Registered successfully"}

    except Exception as e:
        print("REGISTER ERROR:", e)
        return {"message": "Server error during register"}


@app.post("/login")
def login(user: User):
    try:
        db_user = users_collection.find_one({"username": user.username})

        if not db_user:
            return {"message": "User not found"}

        if db_user["password"] != user.password:
            return {"message": "Wrong password"}

        return {"message": "Login successful"}

    except Exception as e:
        print("LOGIN ERROR:", e)
        return {"message": "Server error during login"}


@app.post("/ask")
def ask(q: Question):
    return {"answer": f"You asked: {q.text}"}