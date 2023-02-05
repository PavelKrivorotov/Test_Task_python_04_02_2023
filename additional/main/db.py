from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base


Engine = create_engine(
    "postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/task"
)

Base = declarative_base()

session = Session(Engine)


def init_db() -> None:
    _init_models(Engine)

def _init_models(engine) -> None:
    Base.metadata.create_all(bind=engine)