FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE = 1
ENV PYTHONUNBUFFERED = 1

WORKDIR /code

COPY requirements.txt /code/
RUN python3 -m venv venv && pip install -r requirements.txt

COPY . /code/