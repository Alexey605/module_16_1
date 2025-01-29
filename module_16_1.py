from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home() -> dict:
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def admin_page() -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def user_page(user_id: str) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user/")
async def user_info(user: str = "none", age: str = "none") -> dict:
    return {"message": f"Информация о пользователе. Имя: {user}, Возраст: {age}"}