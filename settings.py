from sqlalchemy.orm import   sessionmaker , DeclarativeBase 
from sqlalchemy import create_engine  
import os 
from dotenv import load_dotenv 

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL") 

class Model(DeclarativeBase):
    pass 

engine = create_engine(
    DATABASE_URL ,
    echo=True 
)

session_local = sessionmaker(autoflush=False , autocommit=False , bind=engine) 

def getdb():
    db = session_local()
    try :
        yield db 
    finally :
        db.close()