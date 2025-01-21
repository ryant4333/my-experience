# from sqlalchemy import create_engine, text, insert

# import time

# time.sleep(5)


# postgresql_url = "postgresql://ryan:4123@postgres_db_container:5432/mydb"

# engine = create_engine(postgresql_url)

# conn = engine.connect()
# query = text(
#     "INSERT INTO projects (project_name, summary, details, tags, start_date, end_date) VALUES ('Experience Portal', 'The page you are on!', 'Detailed summary', NULL, '2025-01-10', '2025-03-01');"
# )
# conn.execute(query)
# conn.commit()

# print("done")


# conn.close()


from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routers import projects

import logging
import os

ENV = os.environ.get("ENV", "development")

# from routers import projects
description = """
My-Experience Backend

## Projects

You can:
 - Add new projects
 - Search and filter exisiting projects
"""

app = FastAPI(title="My-Experience")

api_app = FastAPI(
    title="ChimichangApp", description=description, dependencies=[], version="0.0.1"
)

api_app.include_router(projects.router)

app.mount("/api", api_app, name="api")

if ENV == "production":
    app.mount("/", StaticFiles(directory="static", html=True), name="ui")

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run()
