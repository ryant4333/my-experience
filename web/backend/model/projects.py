from pydantic import BaseModel


class Project(BaseModel):
    project_id: int
    project_name: str
    summary: str
    details: str
    tags: list(str)
    start_date: str
    end_date: str
