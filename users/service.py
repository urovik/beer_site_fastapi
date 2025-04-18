import uuid
from sqlalchemy import select,insert,update,delete
from typing import List

from database.models import async_session,User
from auth.utils import hash_password

class UserService:
    @classmethod
    async def get_user_by_name(cls,name: str) -> User:
        async with async_session() as session:
            query = select(User).where(User.name == name)
            res = await session.execute(query)
            return res.scalar()
    @classmethod
    async def get_user_by_id(cls,id: uuid.UUID) -> User:
        async with async_session() as session:
            query = select(User).where(User.id == id)
            res = await session.execute(query)
            return res.scalar()
    @classmethod
    async def add_users(cls,name,password,email):
        async with async_session() as session:
            new_user = User(
                name = name, 
                email = email,
                password = hash_password(password)
            )
            session.add(new_user)
            await session.commit()
    @classmethod    
    async def delete_users(cls,id: uuid.UUID):
        async with async_session() as session:
            query = delete(User).where(User.id == id)
            await session.execute(query)
            await session.commit()
    @classmethod
    async def update_users(cls,id: uuid.UUID,name,email):
        async with async_session() as session:
            query = update(User).where(User.id == id).values(name = name,email = email)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def get_all_users(cls) -> List[User]:
        async with async_session() as session:
            query = select(User)
            result = await session.execute(query)
            return result.scalars().all()

   