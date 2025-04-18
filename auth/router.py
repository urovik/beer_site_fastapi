from fastapi import APIRouter, Cookie,Depends, Request,Response

from users.schemas import UserBase, UserSchema


import auth.utils as auth_utils
from .dependencies import validate_auth_user,get_current_auth_user,get_current_token_payload_user
from .schemas import TokenInfo

router = APIRouter(prefix = "/api/jwt",tags = ["JWT"])



@router.post('/token')
async def login(response: Response,user: UserSchema = Depends(validate_auth_user)) -> TokenInfo:
    jwt_payload = {
        "sub": str(user.id),
        "name": user.name,
        "email": user.email
    }
    token = auth_utils.encode_jwt(jwt_payload)
     #Устанавливаем токен в куку
    response.set_cookie(
        key="access_token",
        value=token,
        samesite='strict',
        httponly= True,
    )
    return TokenInfo(
        access_token=token,
        token_type="Bearer"
    )

@router.get("/profile")
async def auth_user_profile(
    user: UserBase = Depends(get_current_auth_user)
):
    return {
        "name": user.name,
        "email": user.email
    }
 
@router.post("/logout")
async def logout(
    response: Response
):
    response.delete_cookie(
        key="access_token",
        samesite='strict',
        httponly= True,
    )
    return {"msg":"Вы успешно вышли из аккаунта"}