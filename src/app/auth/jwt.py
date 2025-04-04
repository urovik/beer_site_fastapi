from fastapi import APIRouter, Cookie, Depends, Form, HTTPException, Response,status
from jwt import DecodeError
from src.app.auth.pydantic_model import TokenInfo
import src.app.auth.utils as auth_utils

from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials

import src.database.request as rg

from src.config.pydantics_model import UserSchema


#http_bearer = HTTPBearer()

#oauth2_scheme = OAuth2PasswordBearerWithCookie(tokenUrl="/api/auth/login")
router = APIRouter(prefix = "/api/jwt",tags = ["JWT"])


async def validate_auth_user(
    name: str = Form(),
    password: str = Form()
):
    unauthed_exp = HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail="invalid password or name")
    
    if not (user:= await rg.get_user_by_name(name=name)):
        raise unauthed_exp
    
    if not auth_utils.validate_password(
        password=password,
        hash_password=user.password
    ):
        return unauthed_exp
    return user


async def get_current_token_payload_user(
    access_token: str = Cookie(None)
) -> UserSchema:
    try:
        token = access_token
        if access_token is None:
            raise HTTPException(
                status_code= status.HTTP_401_UNAUTHORIZED,
                detail="token missing"
            )
        payload = auth_utils.decode_jwt(
        token=token
    )
        return payload
    except DecodeError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="token invalid"
        )


async def get_current_auth_user(
    payload: dict = Depends(get_current_token_payload_user)
) -> UserSchema:
    id: str = payload.get("sub")
    if not (user := await rg.get_user_by_id(id=id)):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="not found"
        )
    return user

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
        httponly=True,  # Доступно только для серверных запросов
        samesite="Strict"  # Защита от CSRF
    )
    return TokenInfo(
        access_token=token,
        token_type="Bearer"
    )

@router.get("/profile")
async def auth_user_profile(
    user: UserSchema = Depends(get_current_auth_user)
):
    return {
        "name":user.name,
        "email":user.email
    }
