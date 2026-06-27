import uvicorn 
from fastapi import FastAPI 
from settings import Model , engine 
from src.views import router as pages_routers

app = FastAPI()

app.include_router(pages_routers)

uvicorn.run("main:app", host="0.0.0.0", port=8000)
Model.metadata.create_all(engine)

