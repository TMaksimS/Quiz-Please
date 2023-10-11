from fastapi import APIRouter

from src.api.quiz_handler import app as quiz_handler
from src.api.adapter_handler import app as ask_handler


app = APIRouter(prefix="/api")
app.include_router(quiz_handler)
app.include_router(ask_handler)
