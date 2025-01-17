from fastapi import APIRouter

router = APIRouter(prefix="/projects")


@router.get("/")
def get_projects():
    return "all projects"
