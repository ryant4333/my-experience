from .init import engine
from model.projects import Project, ProjectORM
from sqlalchemy.orm import sessionmaker
from typing import List, Optional

Session = sessionmaker(bind=engine)

class ProjectRepository:
    def get_all(self) -> List[Project]:
        with Session() as session:
            result = session.query(ProjectORM).all()
            return [self.row_to_model(row) for row in result]

    def get_one(self, project_id: int) -> Optional[Project]:
        with Session() as session:
            result = session.query(ProjectORM).filter(ProjectORM.id == project_id).first()
            return self.row_to_model(result) if result else None

    def add(self, project: Project) -> Project:
        with Session() as session:
            project_orm = ProjectORM(**self.model_to_orm(project))
            session.add(project_orm)
            session.commit()
            session.refresh(project_orm)
            return self.row_to_model(project_orm)

    # def replace(self, project_id: int, project: Project) -> Project:
    #     with Session() as session:
    #         project_orm = session.query(ProjectORM).filter(ProjectORM.id == project_id).first()
    #         if project_orm:
    #             for key, value in self.model_to_orm(project).items():
    #                 setattr(project_orm, key, value)
    #             session.commit()
    #             session.refresh(project_orm)
    #             return self.row_to_model(project_orm)
    #         return None

    # def modify(self, project_id: int, project: Project) -> Project:
    #     with Session() as session:
    #         project_orm = session.query(ProjectORM).filter(ProjectORM.id == project_id).first()
    #         if project_orm:
    #             for key, value in self.model_to_orm(project).items():
    #                 if value is not None:
    #                     setattr(project_orm, key, value)
    #             session.commit()
    #             session.refresh(project_orm)
    #             return self.row_to_model(project_orm)
    #         return None

    def delete(self, project_id: int) -> None:
        with Session() as session:
            project_orm = session.query(ProjectORM).filter(ProjectORM.id == project_id).first()
            if project_orm:
                session.delete(project_orm)
                session.commit()

    def row_to_model(self, row: ProjectORM) -> Project:
        return Project(**row.__dict__)

    def model_to_orm(self, project: Project) -> dict:
        return project.model_dump()

# Usage
project_repository = ProjectRepository()
