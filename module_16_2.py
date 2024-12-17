from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
async def read_root() -> dict:
    return "Главная страница"

@app.get("/user/admin")
async def admin_page() -> dict:
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def user_id_page(user_id: int = Path(gt=1, lt=100, description ='Enter User ID', examples='1')) -> dict:
    return f"Вы вошли как пользователь № {user_id}"

@app.get('/user/{username}/{age}')
async def user_inform_page(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', examples='Urban')],
                            age: Annotated[int,Path(gt=18, lt=120, description='Enter age', examples='24')]) -> dict:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

# Запуск: uvicorn module_16_2:app --reload