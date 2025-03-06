from fastapi import FastAPI
import google.generativeai as genai
from pydantic import BaseModel

# Set up API
genai.configure(api_key="AIzaSyBskkOAlcSiRNmHlLb5xunJsktp3S0PB98")

app = FastAPI()

# Define request model
class DebateRequest(BaseModel):
    topic: str

@app.post("/debate/")
async def debate(request: DebateRequest):
    topic = request.topic
    model = genai.GenerativeModel("gemini-2.0-flash")

    response_for = model.generate_content(f"Argue FOR: {topic}").text
    response_against = model.generate_content(f"Argue AGAINST: {topic}").text

    return {"for": response_for, "against": response_against}