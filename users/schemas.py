import uuid
from pydantic import BaseModel,ConfigDict, EmailStr


class UserBase(BaseModel):
    name: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)

class UserCreateSchema(UserBase):
    password: str



class UserSchema(UserBase):
    id: uuid.UUID


class UserUpdateSchema(UserBase):
    pass



