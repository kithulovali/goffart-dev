from fastapi import FastAPI 
from model.models import Resume ,Project , Contact
from settings import Model , engine 
from src.views import router as pages_router 
from apis.views import router as apis_router
import uvicorn 

app = FastAPI()
app.include_router(pages_router)
app.include_router(apis_router, prefix="/admin")

uvicorn.run("main:app",host="0.0.0.0", port=8000)
Model.metadata.create_all(engine)