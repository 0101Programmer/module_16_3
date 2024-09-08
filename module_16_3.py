from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

# python -m uvicorn module_16_3:app

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_all_users() -> dict:
    return users


@app.post('/users/{username}/{age}')
async def new_user(username: Annotated[
    str, Path(min_length=3, max_length=20, description='Enter username', example='Fin')],
                   age: Annotated[int, Path(ge=1, le=100, description='Enter your age', example='15')]) -> str:
    data = f'Имя: {username}, возраст: {str(age)}'
    new_index = str(int(max(users)) + 1)
    users[new_index] = data
    return f'User <{new_index}> is registered'


@app.put('/users/{user_id}/{username}/{age}')
async def upd_user(user_id: Annotated[str, Path(description='Enter your id', example='1')], new_name: str,
                   new_age: str) -> str:
    new_str = f'Имя: {new_name}, возраст: {new_age}'
    users[user_id] = new_str
    return f'The user <{user_id}> was updated'


@app.delete('/user/{user_id}')
def del_user(user_id: Annotated[str, Path(description='Enter user id', example='1')]):
    users.pop(user_id)
    return f'User {user_id} was deleted'
