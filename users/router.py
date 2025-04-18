
from fastapi import APIRouter, Depends

from .schemas import UserCreateSchema, UserSchema, UserUpdateSchema
from .service import UserService
from auth.dependencies import get_current_auth_user

router = APIRouter(prefix="/api/users",tags=["Пользователь"])

@router.get("/all")
async def get_all_user():
    return await UserService.get_all_users()

@router.get("")
async def get_user(user_id: UserSchema = Depends(get_current_auth_user)):
    res = await UserService.get_user_by_id(id = user_id.id)
    return res

@router.post("")
async def add_user(user: UserCreateSchema):
    existing_user = await UserService.get_user_by_name(user.name)
    if existing_user:
        return {"message":"пользователь уже существует"}
    await UserService.add_users(name = user.name,password = user.password,email = user.email)
    return {"status":"200"}

@router.delete("")
async def delete_user(user_id: UserSchema = Depends(get_current_auth_user) ):
    await UserService.delete_users(id = user_id.id)
    return {"message":"юзер удален"}

@router.put("")
async def update_user(user: UserUpdateSchema,user_id: UserSchema = Depends(get_current_auth_user)):
    await UserService.update_users(id = user_id.id, name = user.name,  email = user.email )
    return {"message" : "Данные пользователя обновлены"}
