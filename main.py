import uvicorn
from fastapi import FastAPI, Response

from src.api import app as app_router
from settings import APP_HOST, APP_RELOAD, APP_PORT, LOGER

app = FastAPI(
    title="QUIZ-PLEASE",
    description="Quiz",
    version="0.1",
    contact={
        "name": "Tarkin Maksim",
        "email": "williamcano97@gmail.com"
    },
)
app.include_router(
    router=app_router
)


@app.get("/")
async def curl():
    return Response(content="OK", status_code=200)


@LOGER.catch
def main(host: str, port: int, reload: bool) -> uvicorn:
    return uvicorn.run(
        "main:app",
        host=f"{host}",
        port=port,
        reload=reload
    )


if __name__ == "__main__":
    main(host=APP_HOST, port=APP_PORT, reload=APP_RELOAD)
