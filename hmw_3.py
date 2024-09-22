from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}


# python -m uvicorn hmw_3:app

@app.get('/users')
async def get_all_messages() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def create_user(username: str, age: int):
    new_key = str(int(max(users.keys())) + 1)
    users[new_key] = f'Имя: {username}, возраст: {age}'
    return f'Пользователь с айди {new_key} создан!'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str, username: str, age: str):
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'Пользователь с айди {user_id} обновлён'


@app.delete('/user/{user_id}')
async def delete_user(user_id: str):
    users.pop(user_id)
    return f'Пользователь с айди {user_id} удалён'
