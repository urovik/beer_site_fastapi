from sqlalchemy import select,insert,update,delete
from .models import Product, Type

from database.models import async_session


class ProductService:
    @classmethod
    async def get_all_products_from_db(cls) -> list[Product]:
        async with async_session() as session:
            query = select(Product)
            res = await session.execute(query)
            return res.scalars().all()
    @classmethod
    async def add_products_on_table(cls,name,description,manafacture,type):
        async with async_session() as session:
            query = (insert(Product)
                    .values(name=name, 
                            description=description, 
                            manafacture=manafacture, 
                            type=type))
            res = await session.execute(query)
            await session.commit()
    @classmethod
    async def get_product_by_name(cls,name):
        async with async_session() as session:
            query = select(Product).where(Product.name == name)
            res = await session.execute(query)
            return res.scalar()
    @classmethod   
    async def add_type_product_on_table(cls,type):
        async with async_session() as session:
            query = insert(Type).values(type = type)
            await session.execute(query)
            await session.commit()
    @classmethod
    async def get_type_from_db(cls,type) -> Type:
        async with async_session() as session:
            query = select(Type).where(Type.type == type)
            res = await session.execute(query)
            return res.scalar()
    @classmethod
    async def get_all_type_products_from_db(cls) -> list[Type]:
        async with async_session() as session:
            query = select(Type)
            res = await session.execute(query)
            return res.scalars().all()