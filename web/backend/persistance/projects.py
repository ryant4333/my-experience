from .init import engine
from model.projects import Project, ProjectORM
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=engine)


def get_all() -> Project:
    with Session() as session:
        result = session.query(ProjectORM)
        return result


def add(project: Project):
    with Session() as session:
        proj = 
        session.add(post)


def row_to_model(row: tuple) -> Project:
    return Project(**row)


def model_to_orm(project: Project) -> dict:
    return project.model_dump()


get_one()
#     with engine.connect() as conn:

#         qry = "select * from projects where projects=:project"
#         params = ""
#         conn.commit()

# def get_all() -> list[Project]:
