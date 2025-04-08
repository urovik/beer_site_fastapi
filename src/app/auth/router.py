from fastapi import APIRouter,Depends,Response

from auth.dependencies import get_current_auth_user, validate_auth_user
from src.app.auth.schemas import TokenInfo

import utils as auth_utils

from src.config.schemas import UserSchema,UserBase



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
 

