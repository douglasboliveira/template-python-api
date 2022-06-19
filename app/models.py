from typing import Optional
from sqlmodel import SQLModel, Field, Relationship


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str
    hashed_password: str
    is_active: bool = Field(default=True)

    items: "Item" = Relationship(back_populates="user")


class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    user_id: int = Field(foreign_key="user.id")

    user: User = Relationship(back_populates="item")