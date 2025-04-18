from typing import Optional
from sqlalchemy.orm import mapped_column,Mapped
from database.Base import Base
import uuid

from sqlalchemy.dialects.postgresql import UUID


class User(Base):
    __tablename__ = "users"
    id: Mapped[uuid.UUID] = mapped_column(
        UUID, primary_key=True, index=True, default=uuid.uuid4)
    name: Mapped[str]
    email: Mapped[Optional[str]]
    password: Mapped[bytes]

