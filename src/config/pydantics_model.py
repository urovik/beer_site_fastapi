
from pydantic import BaseModel,ConfigDict, EmailStr


class UserSchema(BaseModel):
    name: str
    password: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)


