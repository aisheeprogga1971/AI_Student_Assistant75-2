from fastapi import APIRouter, Query
from pydantic import BaseModel
from auth import decode_token
import openai

router = APIRouter()

openai.api_key = "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"

class Question(BaseModel):
    text: str

@router.post("/ask")
def ask(question: Question, token: str = Query(None)):

    user = "Guest"

    if token:
        try:
            payload = decode_token(token)
            user = payload["sub"]
        except:
            user = "Guest"

    # 🎯 THIS IS YOUR PROMPT
    prompt = f"""
    You are an AI Student Assistant.

    Your job:
    - Help students from any background
    - Give clear, simple, structured answers
    - If question is academic, explain step-by-step

    Student ({user}) asked:
    {question.text}
    """

    # 🤖 AI CALL
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful AI tutor."},
            {"role": "user", "content": prompt}
        ]
    )

    answer = response["choices"][0]["message"]["content"]

    return {"answer": answer}