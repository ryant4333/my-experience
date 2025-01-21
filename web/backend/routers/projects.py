from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..model.projects import Projects

# from service.projects import ProjectService
# from persistance.projects import Session
from sqlmodel import select

import os
from sqlmodel import create_engine, Session

tags_metadata = [{"name"}]

router = APIRouter(prefix="/projects")


DB_NAME = "mydb"
DB_PORT = "5432"
# DB_HOST = "postgres_db_container"
DB_HOST = "localhost"
DB_PASSWORD = "4123"
DB_USER = "ryan"

postgresql_url = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(postgresql_url)


# @router.get("/", response_model=List[Project])
@router.get("/")
def get_projects():
    with Session(engine) as session:
        projects = session.exec(select(Projects)).all()
        return projects
    # return service.get_all()


# tag_to_filter = "example_tag"

#     # Create the query
#     query = select(Item).where(Item.tags.contains([tag_to_filter]))

#     # Execute the query
#     results = session.exec(query).all()


# @router.get("/{project_id}", response_model=Project)
# def get_project(project_id: int, service: ProjectService = Depends()):
#     project = service.get_one(project_id)
#     if not project:
#         raise HTTPException(status_code=404, detail="Project not found")
#     return project


@router.post("/", response_model=Projects)
def create_project(project: Projects):

    with Session(engine) as session:
        session.add(project)
        session.commit()
        session.refresh(project)
        return project
    # return service.create(project)


# @router.put("/{project_id}", response_model=Project)
# def replace_project(project_id: int, project: ProjectUpdate, service: ProjectService = Depends()):
#     return service.replace(project_id, project)

# @router.patch("/{project_id}", response_model=Project)
# def modify_project(project_id: int, project: ProjectUpdate, service: ProjectService = Depends()):
#     return service.modify(project_id, project)


# @router.delete("/{project_id}")
# def delete_project(project_id: int, service: ProjectService = Depends()):
#     service.delete(project_id)
#     return {"detail": "Project deleted"}
