import uuid

from .models import User
from .models import async_session

from sqlalchemy import select,insert,update,delete
from app.auth.utils import hash_password

from typing import List



async def get_user_by_name(name: str) -> User:
    async with async_session() as session:
        query = select(User).where(User.name == name)
        res = await session.execute(query)
        return res.scalar()

async def get_user_by_id(id: uuid.UUID) -> User:
    async with async_session() as session:
        query = select(User).where(User.id == id)
        res = await session.execute(query)
        return res.scalar()

async def add_users(name,password,email):
    async with async_session() as session:
        new_user = User(
            name = name, 
            email = email,
            password = hash_password(password)
        )
        session.add(new_user)
        await session.commit()
    
async def delete_users(id: uuid.UUID):
    async with async_session() as session:
        query = delete(User).where(User.id == id)
        await session.execute(query)
        await session.commit()

async def update_users(id: uuid.UUID,name,email):
    async with async_session() as session:
        query = update(User).where(User.id == id).values(name = name,email = email)
        await session.execute(query)
        await session.commit()


async def get_all_users() -> List[User]:
    async with async_session() as session:
        query = select(User)
        result = await session.execute(query)
        return result.scalars().all()

   