import os
from sqlmodel import create_engine

# from sqlalchemy import create_engine
# from sqlalchemy.engine import Engine


# engine: Engine | None = None

DB_NAME = "mydb"
DB_PORT = "5432"
DB_HOST = "postgres_db_container"
DB_PASSWORD = "4123"
DB_USER = "ryan"


def get_db(name: str | None = None, reset: bool = False):
    global engine
    # swap for env
    postgresql_url = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    engine = create_engine(postgresql_url)


get_db()
