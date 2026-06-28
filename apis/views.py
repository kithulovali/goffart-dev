from fastapi  import APIRouter , Depends 
from model.models import Contact , Resume , Project 
from model.serializer import ReadFeedBack , ReadProject , ReadResume , CreateProject ,CreateResume , SendFeedBack , UpdateProject , UpdateResume 
from settings import getdb 
from sqlalchemy.orm import Session


router = APIRouter()

# resume endpoints

@router.post("/resume")
async def create_resume():
    return 

@router.put("/resume")
async def update_resume():
    return 

@router.get("/resume")
async def list_resume():
    return 

# project endpoints

@router.post("/project")
async def create_project():
    return 

@router.put("/project")
async def update_project():
    return 

@router.get("/project")
async def list_projects():
    return 

# read feedbacks 
@router.get("/contact")
async def list_messages():
    return 