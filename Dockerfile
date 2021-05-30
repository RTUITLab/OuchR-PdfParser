FROM python:3.8.6-alpine

# рабочая директория внутри проекта
WORKDIR /usr/src/app

# Устанавливаем зависимости для Postgre
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
RUN apk --update --upgrade add gcc

# устанавливаем зависимости
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .
