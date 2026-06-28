from model.models import Contact , Project , Resume 
from model.serializer import CreateProject ,CreateResume , UpdateProject , UpdateResume , ReadFeedBack , ReadProject ,ReadResume , SendFeedBack 
from fastapi import APIRouter , Depends , Request 
from settings import  getdb  
from fastapi.templating import Jinja2Templates 
from fastapi.staticfiles import StaticFiles 

router = APIRouter()
templating = Jinja2Templates(directory="templates")
router.mount("/static", StaticFiles(directory="static"), name="static")


@router.get("/", include_in_schema=False)
async def home(request : Request):
    return templating.TemplateResponse(request , "home.html")

@router.get("/projects", include_in_schema=False)
async def list_projects(request : Request):
    return templating.TemplateResponse(request , 'project_list.html')

@router.get("/resume", include_in_schema=False)
async def render_resume(request : Request):
    return templating.TemplateResponse(request , "resume.html")

@router.post("/contact", include_in_schema=False)
async def send_messages(request : Request):
    return templating.TemplateResponse(request ,"contact.html" )
