from fastapi import APIRouter , Depends
from model.models import Project , Contact  
from model.serializer import CreateProject , UpdateProject , SendMessage , ProjectResponse
from settings import session_local , getdb 


router = APIRouter()

@router.post("/project")
async def new_project():
    return 


@router.put("/project")
async def update_project():
    return 

