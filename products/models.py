
from sqlalchemy.orm import mapped_column,Mapped
from sqlalchemy import ForeignKey, SmallInteger, String
from database.Base import Base

class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(70))
    description: Mapped[str]
    manafacture: Mapped[str] = mapped_column(String(100))
    type: Mapped[str] = mapped_column(String(20),ForeignKey("type_products.type",ondelete="CASCADE"))

class Snacks(Base):
    __tablename__ = "snacks"
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id",ondelete="CASCADE"),primary_key=True)
    is_spicy: Mapped[bool] = mapped_column()
    calories: Mapped[int] = mapped_column(SmallInteger)  

class Drinks(Base):
    __tablename__ = "drinks"
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id",ondelete="CASCADE"),primary_key=True)
    volume: Mapped[float]
    type: Mapped[str] = mapped_column(String(30))
    is_alcohol: Mapped[bool] = mapped_column()
    strength: Mapped[float | None] = mapped_column(SmallInteger) 


class Type(Base):
    __tablename__ = "type_products"
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(20),nullable=False,unique=True)