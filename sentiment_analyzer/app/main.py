from fastapi import APIRouter, FastAPI
from pydantic import BaseModel
from app.services.sentiment import analyze_sentiment

router = APIRouter()

class TextInput(BaseModel):
    text: str

@router.post("/analyze")
def analyze(input: TextInput):
    result = analyze_sentiment(input.text)
    return {"sentiment": result}
app = FastAPI()
app.include_router(router)