from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, null
from sqlalchemy.orm import relationship

from .database import Base

# one to many relationship com relação obrigatória dos dois lados

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    item = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)

    # owner_id referencia users(id)
    # Setando como campo obrigatório garante pelo menos um registro
    owner_id = Column(Integer, ForeignKey("users.id"), nullable = False)

    owner = relationship("User", back_populates="item")