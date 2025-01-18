from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import ARRAY

Base = declarative_base()


class Project(BaseModel):
    project_id: int
    project_name: str
    summary: str
    details: str
    tags: List[str]
    start_date: str
    end_date: str

class ProjectCreate(BaseModel):
    project_name: str
    summary: str
    details: str
    tags: Optional[List[str]]
    start_date: str
    end_date: str


class ProjectORM(Base):
    __tablename__ = "projects"

    project_id = Column(Integer, autoincrement=True, primary_key=True)
    project_name = Column(String)
    summary = Column(String)
    details = Column(String)
    tags = Column(ARRAY(String), nullable=True)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
