from sqlmodel import Session

from . import models, schemas


def get_user(session: Session, user_id: int):
    return session.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(session: Session, email: str):
    return session.query(models.User).filter(models.User.email == email).first()


def get_users(session: Session, skip: int = 0, limit: int = 100):
    return session.query(models.User).offset(skip).limit(limit).all()


def create_user(session: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    session_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    session.add(session_user)
    session.commit()
    session.refresh(session_user)
    return session_user


def get_items(session: Session, skip: int = 0, limit: int = 100):
    return session.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(session: Session, item: schemas.ItemCreate, user_id: int):
    session_item = models.Item(**item.dict(), user_id=user_id)
    session.add(session_item)
    session.commit()
    session.refresh(session_item)
    return session_item
