import time
import requests as r

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

from . import settings
from . import constants


def get_response(
        url: str = constants.DEFAULT_URL,
        query: str = constants.DEFAULT_QUERY_PARAMS
    ) -> dict:
    
    response = r.post(url=url, json={"query":query})

    if response.status_code != 200:
        raise ValueError("Not correct request.")

    json = response.json()
    return json

def check_db_connect(
    start_period: int = 5,
    interval: int = 5,
    retries: int = 3
    ) -> None:
    
    time.sleep(start_period)

    count = 0
    while count < retries:
        engine = create_engine(
            "".join([
                f"postgresql+psycopg2://",
                f"{settings.PG_USERNAME}:",
                f"{settings.PG_PPASSWORD}@",
                f"{settings.PG_HOST}:",
                f"{settings.PG_PORT}/",
                f"{settings.PG_DATABASE_NAME}"
            ])
        )

        try:
            conn = engine.connect()
            conn.close()

            print("Complete connect to database.")

            return None
        except SQLAlchemyError as err:
            print(f"Falied connection to database {count}.")

            time.sleep(interval)
            count += 1
    
    raise ConnectionError("Can`t connect to database.")