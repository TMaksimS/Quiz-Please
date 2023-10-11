import datetime

from sqlalchemy import String, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import TIMESTAMP

from ..database import Base


class Category(Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True
    )
    name: Mapped[str] = mapped_column(
        String(225), nullable=False, unique=True,
        name="Название категории"
    )
    questions: Mapped["Question"] = relationship(
        uselist=True, back_populates="category", lazy=False
    )


class Question(Base):
    __tablename__ = "questions"
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True
    )
    ques: Mapped[str] = mapped_column(
        String(525), unique=True, nullable=False, name="Вопрос из викторины"
    )
    answer: Mapped[str] = mapped_column(
        String(125), nullable=False, name="Ответ на вопрос"
    )
    created_at: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP(timezone=True), nullable=False, name="Дата создания"
    )
    on_site: Mapped[int] = mapped_column(
        Integer, unique=True, nullable=False,
        name="Номер записи на сайта"
    )
    category_id: Mapped[int] = mapped_column(
        ForeignKey(column="categories.id", ondelete="CASCADE")
    )
    category: Mapped["Category"] = relationship(
        back_populates="questions"
    )
