from sqlalchemy import select,insert,update,delete
from src.app.auth.utils import hash_password
from src.database.models import User
from src.database.models import async_session
from src.config.pydantics_model import UserSchema
from typing import List



async def get_user(name: str) -> UserSchema:
    async with async_session() as session:
        query = select(User).where(User.name == name)
        res = await session.execute(query)
        return res.scalar()

async def add_users(name,password,email):
    async with async_session() as session:
        new_user = User(
            name = name, 
            email = email,
            password = hash_password(password=password)
           
        )
        session.add(new_user)
        await session.commit()
    
async def delete_users(id: int):
    async with async_session() as session:
        query = delete(User).where(User.id == id)
        await session.execute(query)
        await session.commit()

async def update_users(id: int, name: str, email: str ):
    async with async_session() as session:
        query = update(User).where(User.id == id).values(name = name,email = email )
        await session.execute(query)
        await session.commit()


async def get_all_users() -> List[UserSchema]:
    async with async_session() as session:
        query = select(User)
        result = await session.execute(query)
        return result.scalars().all()

   