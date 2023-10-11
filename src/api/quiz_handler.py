from fastapi import APIRouter, Depends
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.crud import CategoryDB
from src.database.schemas import GetCategory, ResponseQue, ResponseQueWithPage
from src.database import get_db
from settings import LOGER

app = APIRouter(prefix="/quiz", tags=["quiz"])


@app.post("/category={cat_id}")
@LOGER.catch
async def get_category(
        cat_id: int,
        session: AsyncSession = Depends(get_db)
):
    """Возвращает категорию с вопросами если указанный id существует в БД"""
    data = CategoryDB(session=session)
    result = await data.get_category_id(category_id=cat_id)
    if result:
        questions = await data.get_question_by_category_id(result.id)
        return GetCategory(
            id=result.id,
            name=result.name,
            questions=questions
        )
    return HTTPException(status_code=404, detail="Data not found")


@app.post("/question={que_id}")
@LOGER.catch
async def get_question(
        que_id: int,
        session: AsyncSession = Depends(get_db)
):
    """Возвращает вопрос по ID если такой существует"""
    data = CategoryDB(session=session)
    result = await data.get_question_id(question_id=que_id)
    if result:
        return ResponseQue.model_validate(result)
    return HTTPException(status_code=404, detail="Data not found")


@app.get("/questions")
@LOGER.catch
async def get_all_questions(
        limit: int,
        offset: int,
        session: AsyncSession = Depends(get_db)
):
    """Возвращает limit вопросов в одном ответе"""
    data = CategoryDB(session=session)
    result = await data.get_question_with_page(limit=limit, offset=offset)
    if result[0]:
        return ResponseQueWithPage(
            data=result,
            limit=limit,
            offset=offset,
        )
    return HTTPException(status_code=404, detail="Data not found")
