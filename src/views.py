from fastapi import APIRouter , Request 
from fastapi.templating import Jinja2Templates 
from fastapi.staticfiles import StaticFiles 
from model.models import Project , Contact 
from model.serializer import CreateProject , UpdateProject , SendMessage , ProjectResponse

router = APIRouter()
templates = Jinja2Templates(directory="templates")
router.mount("/static" , StaticFiles(directory="static"), name="static")

@router.get("/")
async def home(request : Request):
    return templates.TemplateResponse(request , "home.html")


@router.get("/project")
async def project_list(request : Request):
    return templates.TemplateResponse(request , "project_list.html")