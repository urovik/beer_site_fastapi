import uuid
from pydantic import BaseModel,ConfigDict, EmailStr


class UserCreate(BaseModel):
    name: str
    password: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)


class UserSchema(BaseModel):
    id: uuid.UUID
    



