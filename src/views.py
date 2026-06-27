from fastapi import APIRouter , Request 
from fastapi.templating import Jinja2Templates 
from fastapi.staticfiles import StaticFiles 
from model.models import Project , Contact 
from model.serializer import Create_Project , Update_Project , Send_Message

router = APIRouter()
templates = Jinja2Templates(directory="/tempaltes")
router.mount("/static" , StaticFiles(directory="static"), name="static")

@router.router("/")
async def home(request : Request):
    return templates.TemplateResponse(request , "home.html")