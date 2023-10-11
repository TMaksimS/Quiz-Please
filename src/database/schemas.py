import datetime

from pydantic import BaseModel, ConfigDict


class MyModel(BaseModel):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)


class CreateCategory(MyModel):
    """Для создания категории"""
    name: str


class GetQuestionBySite(MyModel):
    """Для валидации вопроса с сайта"""
    ques: str
    answer: str
    category: CreateCategory
    created_at: datetime.datetime
    on_site: int


class GetQuestion(GetQuestionBySite):
    """Для API ответа модели вопроса"""
    id: int


class CreateQuestion(MyModel):
    """Для создания вопроса в БД"""
    ques: str
    answer: str
    created_at: datetime.datetime
    on_site: int


class GetCategory(MyModel):
    """Для валидации категории с вопрсами"""
    id: int
    name: str
    questions: list[GetQuestion]


class ResponseQue(MyModel):
    """Для валидации вопроса из БД"""
    id: int
    ques: str
    answer: str
    category_id: int
    created_at: datetime.datetime
    on_site: int


class ResponseQueWithPage(MyModel):
    """Для списка вопросов с пагинацией"""
    data: list[ResponseQue]
    limit: int
    offset: int
