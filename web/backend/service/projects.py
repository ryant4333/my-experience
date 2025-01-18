from typing import List
from model.projects import Project, ProjectCreate, ProjectUpdate
from persistance import project_repository
from fastapi import HTTPException

class ProjectService:
    def get_all(self) -> List[Project]:
        return project_repository.get_all()

    def get_one(self, project_id: int) -> Project:
        project = project_repository.get_one(project_id)
        if not project:
            raise HTTPException(status_code=404, detail="Project not found")
        return project

    def create(self, project: ProjectCreate) -> Project:
        return project_repository.add(Project(**project.dict()))

    # def replace(self, project_id: int, project: ProjectUpdate) -> Project:
    #     existing_project = project_repository.get_one(project_id)
    #     if not existing_project:
    #         raise HTTPException(status_code=404, detail="Project not found")
    #     return project_repository.replace(project_id, Project(**project.dict()))

    # def modify(self, project_id: int, project: ProjectUpdate) -> Project:
    #     existing_project = project_repository.get_one(project_id)
    #     if not existing_project:
    #         raise HTTPException(status_code=404, detail="Project not found")
    #     return project_repository.modify(project_id, Project(**project.dict()))

    def delete(self, project_id: int) -> None:
        existing_project = project_repository.get_one(project_id)
        if not existing_project:
            raise HTTPException(status_code=404, detail="Project not found")
        project_repository.delete(project_id)