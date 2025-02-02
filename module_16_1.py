from fastapi import FastAPI

app = FastAPI()

@app.get("/user/{username}/{age}")
async def read_user_info(username: str, age: int):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

@app.get("/user/admin")
async def read_adm():
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def read_user_id(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/")
async def read_root():
    return {"message": "Главная страница"}