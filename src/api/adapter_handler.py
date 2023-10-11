from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.crud import CategoryDB
from src.database.schemas import CreateQuestion, GetQuestion
from src.database import get_db
from src.collector import Collector
from settings import LOGER

app = APIRouter(prefix="/site", tags=["adapter"])


@app.post("/")
@LOGER.catch
async def create_questions(
        questions_num: int,
        session: AsyncSession = Depends(get_db)
) -> GetQuestion:
    """Создает новые записи в БД"""
    connectdb = CategoryDB(session=session)
    req = Collector()
    reqdata = await req.parser(await req.get_json(questions_num))
    result = ""
    for i in reqdata:
        data = await connectdb.add_category(
            name=i.category.name,
            body_question=CreateQuestion(
                ques=i.ques,
                answer=i.answer,
                created_at=i.created_at,
                on_site=i.on_site
            ))
        if data:
            result = data
        else:
            while data is None:
                new_req = await req.parser(await req.get_json(1))
                for k in new_req:
                    data = await connectdb.add_category(
                        name=k.category.name,
                        body_question=CreateQuestion(
                            ques=k.ques,
                            answer=k.answer,
                            created_at=k.created_at,
                            on_site=k.on_site,
                        ))
                    result = data
    return result
