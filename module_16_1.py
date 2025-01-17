from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home() -> str:
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def admin_page() -> str:
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def user_page(user_id: int) -> str:
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user/")
async def user_info(username: str, age: int) -> str:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}