from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import users_collection
from auth import hash_password, verify_password, create_token

router = APIRouter()

class User(BaseModel):
    username: str
    password: str

@router.post("/register")
def register(user: User):
    if users_collection.find_one({"username": user.username}):
        raise HTTPException(status_code=400, detail="User exists")

    users_collection.insert_one({
        "username": user.username,
        "password": hash_password(user.password)
    })

    return {"message": "Registered successfully"}

@router.post("/login")
def login(user: User):
    db_user = users_collection.find_one({"username": user.username})

    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({"sub": user.username})
    return {"access_token": token}