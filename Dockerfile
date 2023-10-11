FROM python:3.10-slim
RUN apt-get update && apt-get install curl --yes
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
WORKDIR .