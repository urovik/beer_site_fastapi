import uuid
from fastapi import APIRouter

from src.config.pydantics_model import UserCreate, UserSchema

import src.database.request as rq

router = APIRouter(prefix="/api/users",tags=["Пользователь"])

@router.get("/all")
async def get_all_user():
    return await rq.get_all_users()

@router.get("/{user_id}")
async def get_user(user_id: uuid.UUID):
    res = await rq.get_user_by_id(id = user_id)
    return res

@router.post("")
async def add_user(user: UserCreate):
    existing_user = await rq.get_user_by_name(user.name)
    if existing_user:
        return {"message":"пользователь уже существует"}
    await rq.add_users(name = user.name,password = user.password,email = user.email)
    return {"status":"200"}

@router.delete("/{user_id}")
async def delete_user(user_id: uuid.UUID):
    await rq.delete_users(id = user_id)
    return {"message":"юзер удален"}

@router.put("/{user_id}")
async def update_user(user_id: uuid.UUID, user: UserCreate):
    await rq.update_users(id = user_id, name = user.name,  email = user.email )
    return {"message" : "Данные пользователя обновлены"}
