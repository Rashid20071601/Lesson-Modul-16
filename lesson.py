# Импорт библиотек
from fastapi import FastAPI, Path
from typing import Annotated

# Создание экземпляра FastAPI
app = FastAPI()



# Определение маршрутов
@app.get('/')  # Главная страница
async def welcome() -> dict:
    return {'message': 'Hello, world!'}


@app.get('/main')  # Основная страница
async def welcome() -> dict:
    return {'message': 'Main page'}


@app.get('/id')  # Страница с параметрами по умолчанию
async def id_paginator(username: str = "Rashid", age: int = 17) -> dict:
    return {'User': username, 'Age': age}


@app.get('/user/{username}/{id}')  # Страница с валидацией параметров
async def news(
    username: str = Path(min_length=3, max_length=15, description='Enter your name', example='montes'),
    id: int = Path(ge=0, le=1000, description='Enter your id', example='555')
) -> dict:
    return {'message': f'Hello, {username}:{id}'}


@app.get('/users/{username}/{id}')  # Страница с использованием Annotated для параметров
async def news(
    username: Annotated[str, Path(min_length=3, max_length=15, description='Enter your name', example='montes')],
    id: int
) -> dict:
    return {'message': f'Hello, {username}:{id}'}
