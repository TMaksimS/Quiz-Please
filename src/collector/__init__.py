import requests

from src.database.schemas import GetQuestionBySite, CreateCategory


class Collector:
    def __init__(self):
        self.url = "https://jservice.io/api/random?count="

    async def get_json(self, count: int) -> list:
        data = requests.get(url=f"{self.url}{count}")
        return data.json()

    @staticmethod
    async def parser(data: list) -> list[GetQuestionBySite]:
        result = []
        for i in data:
            result.append(GetQuestionBySite(
                ques=i["question"],
                answer=i["answer"],
                category=CreateCategory(name=i["category"]["title"]),
                created_at=i["airdate"],
                on_site=i["id"]
            ))
        return result
