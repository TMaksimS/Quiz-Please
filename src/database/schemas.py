import datetime

from pydantic import BaseModel, ConfigDict


class MyModel(BaseModel):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)


class CreateCategory(MyModel):
    name: str


class GetQuestionBySite(MyModel):
    ques: str
    answer: str
    category: CreateCategory
    created_at: datetime.datetime
    on_site: int


class GetQuestion(GetQuestionBySite):
    id: int


class CreateQuestion(MyModel):
    ques: str
    answer: str
    created_at: datetime.datetime
    on_site: int


class GetCategory(MyModel):
    id: int
    name: str
    questions: list[GetQuestion]


class ResponseQue(MyModel):
    id: int
    ques: str
    answer: str
    category_id: int
    created_at: datetime.datetime
    on_site: int


class ResponseQueWithPage(MyModel):
    data: list[ResponseQue]
    limit: int
    offset: int
