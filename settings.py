from sqlalchemy.orm import DeclarativeBase , sessionmaker
from sqlalchemy import  create_engine 
from dotenv import load_env 
import os 

load_env()
class Model(DeclarativeBase):
    pass 

DATABASE_URL = os.getenv("DATABASE_URL") 

engine = create_engine(
    DATABASE_URL ,
    echo = True
)

sessionLocal = sessionmaker(autoflush=False , autocommit=False , bind=engine)

def getdb():
    db = sessionLocal()
    try :
        yield db 
    finally :
        db.close()