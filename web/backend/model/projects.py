from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime, date
from sqlmodel import Field, SQLModel, ARRAY, Column


class ProjectsBase(SQLModel):
    project_name: str
    summary: str
    tags: List[str] = Field(sa_column=Column(ARRAY(str)))
    start_date: date
    end_date: date


class Projects(ProjectsBase, table=True):
    project_id: Optional[int] = Field(default=None, primary_key=True)


# class Project(BaseModel):
#     project_id: int
#     project_name: str
#     summary: str
#     details: str
#     tags: List[str]
#     start_date: str
#     end_date: str


# class ProjectCreate(BaseModel):
#     project_name: str
#     summary: str
#     details: str
#     tags: Optional[List[str]]
#     start_date: str
#     end_date: str


# class ProjectORM(Base):
#     __tablename__ = "projects"

#     project_id = Column(Integer, autoincrement=True, primary_key=True)
#     project_name = Column(String)
#     summary = Column(String)
#     details = Column(String)
#     tags = Column(ARRAY(String), nullable=True)
#     start_date = Column(DateTime)
#     end_date = Column(DateTime)
