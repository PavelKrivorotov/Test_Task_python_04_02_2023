from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base

from . import settings

Engine = create_engine(
    "".join([
        f"postgresql+psycopg2://",
        f"{settings.PG_USERNAME}:",
        f"{settings.PG_PPASSWORD}@",
        f"{settings.PG_HOST}:",
        f"{settings.PG_PORT}/",
        f"{settings.PG_DATABASE_NAME}"
    ])
)

Base = declarative_base()

session = Session(Engine)


def init_db() -> None:
    _init_models(Engine)

def _init_models(engine) -> None:
    Base.metadata.create_all(bind=engine)

def close_session():
    session.close_all()