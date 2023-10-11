from typing import Sequence, Type

import sqlalchemy.exc
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.database.models import Category, Question
from src.database.schemas import CreateQuestion, GetQuestion


class CategoryDB:
    """Класс для взаимодействия с БД"""
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_category(
            self,
            name: str,
            body_question: CreateQuestion
    ) -> GetQuestion | None:
        """Метод реализует логику добавления новых категорий и вопросов в БД"""
        data = Category(name=name)
        try:
            data.questions = Question(**body_question.model_dump())
            self.session.add(data)
            await self.session.commit()
            return GetQuestion.model_validate(data.questions)
        except sqlalchemy.exc.IntegrityError:
            await self.session.rollback()
            stmt = select(Category).where(Category.name == name)
            obj = await self.session.scalar(stmt)
            if obj:
                try:
                    new_que = Question(**body_question.model_dump())
                    new_que.category_id = obj.id
                    self.session.add(new_que)
                    await self.session.commit()
                    return GetQuestion.model_validate(new_que)
                except sqlalchemy.exc.IntegrityError:
                    await self.session.rollback()
        return None

    async def get_category_id(self, category_id: int) -> Type[Category]:
        """Метод возвращает категорию по id"""
        data = await self.session.get(Category, category_id)
        if data:
            return data

    async def get_question_by_category_id(self, category_id: int):
        """Метод возвращает все вопросы из категории"""
        stmt = select(Question).where(Question.category_id == category_id)
        data = await self.session.scalars(stmt)
        return data.all()

    async def get_question_id(self, question_id: int) -> Type[Question] | None:
        """Метод возвращает вопрос по id"""
        data = await self.session.get(Question, question_id)
        if data:
            return data
        return None

    async def get_question_with_page(self, limit: int, offset: int) -> Sequence[Question]:
        """Метод возвращает вопросы с пагинацией"""
        stmt = select(Question).limit(limit).offset((offset - 1) * limit)
        data = await self.session.scalars(stmt)
        return data.all()
