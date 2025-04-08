from typing import Optional
import uuid
from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker
from sqlalchemy.orm import mapped_column,Mapped

from sqlalchemy.dialects.postgresql import UUID

from .Base import Base
from src.config.settings import Settings



engine = create_async_engine(f'postgresql+asyncpg://{Settings.user_db}:{Settings.password_db}@{Settings.host_db}/{Settings.name_db}')

async_session = async_sessionmaker(bind=engine)




class User(Base):
    __tablename__ = "users"
    id: Mapped[uuid.UUID] = mapped_column(
        UUID, primary_key=True, index=True, default=uuid.uuid4)
    name: Mapped[str]
    email: Mapped[Optional[str]]
    password: Mapped[bytes]

class employee(Base):
    __tablename__ = "employee"
    work_id: Mapped[int] = mapped_column(primary_key=True)



async def db_init():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)  