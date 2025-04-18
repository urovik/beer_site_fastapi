

from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker


from .Base import Base
from config.pydantics_settings import db_config 



engine = create_async_engine(f'postgresql+asyncpg://{db_config.user_db}:{db_config.password_db}@{db_config.host}/{db_config.db_name}')

async_session = async_sessionmaker(bind=engine)





async def db_init():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)  