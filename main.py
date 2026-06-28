from fastapi import FastAPI 
from model.models import Resume ,Project , Contact
from settings import Model , engine 

import uvicorn

app = FastAPI()

uvicorn.run("main:app",host="0.0.0.0", port=8000 )
Model.metadata.create_all(engine)