from fastapi import Cookie, Depends, Form, HTTPException, status
from jwt import DecodeError


from users.schemas import UserSchema
from users.service import UserService
import auth.utils as auth_utils

async def validate_auth_user(
    name: str = Form(),
    password: str = Form()
):
    unauthed_exp = HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail="invalid password or name")
    
    if not (user:= await UserService.get_user_by_name(name=name)):
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
    if not (user := await UserService.get_user_by_id(id=id)):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="not found"
        )
    return user

    