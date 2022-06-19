from sqlmodel import create_engine, SQLModel, Session



SQLMODEL_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"


engine = create_engine(SQLMODEL_DATABASE_URL, echo=False)


SQLModel.metadata.create_all(bind=engine)


def get_session() -> Session:
    return Session(engine)