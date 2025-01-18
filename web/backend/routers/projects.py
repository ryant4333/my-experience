from fastapi import APIRouter, Depends, HTTPException
from typing import List
from model.projects import Project, ProjectCreate
from service.projects import ProjectService

router = APIRouter(prefix="/projects")


@router.get("/", response_model=List[Project])
def get_all_projects(service: ProjectService = Depends()):
    return service.get_all()

@router.get("/{project_id}", response_model=Project)
def get_project(project_id: int, service: ProjectService = Depends()):
    project = service.get_one(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.post("/", response_model=Project)
def create_project(project: ProjectCreate, service: ProjectService = Depends()):
    return service.create(project)

# @router.put("/{project_id}", response_model=Project)
# def replace_project(project_id: int, project: ProjectUpdate, service: ProjectService = Depends()):
#     return service.replace(project_id, project)

# @router.patch("/{project_id}", response_model=Project)
# def modify_project(project_id: int, project: ProjectUpdate, service: ProjectService = Depends()):
#     return service.modify(project_id, project)

@router.delete("/{project_id}")
def delete_project(project_id: int, service: ProjectService = Depends()):
    service.delete(project_id)
    return {"detail": "Project deleted"}