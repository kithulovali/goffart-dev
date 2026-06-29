from fastapi import FastAPI 
from model.models import Resume ,Project , Contact
from settings import Model , engine 
from src.views import router as pages_router 
from apis.views import router as apis_router


app = FastAPI()
app.include_router(pages_router)
app.include_router(apis_router, prefix="/admin")


Model.metadata.create_all(engine)