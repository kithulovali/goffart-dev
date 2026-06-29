from sqlalchemy.orm import Mapped , mapped_column 
from sqlalchemy import DateTime , String ,func , Text
from settings import Model 
from datetime import datetime

class Project(Model):
    __tablename__ = "Projects"

    id : Mapped[int] = mapped_column(primary_key=True , unique=True , index=True ,nullable=False)
    name : Mapped[str] = mapped_column(String(64), nullable=False)
    description : Mapped[str] = mapped_column(String(64), nullable=True)
    banner : Mapped[str] = mapped_column(String(64), nullable=True)
    source : Mapped[str] = mapped_column(String(64), nullable=True)
    created_at : Mapped[datetime] = mapped_column(DateTime,server_default=func.now())

    def __repr__(self):
        return f"{self.name} project"


class Contact(Model):
    __tablename__ = "contacts"

    id : Mapped[int] = mapped_column(primary_key=True , unique=True , index=True , nullable=False)
    name : Mapped[str] = mapped_column(String(64),nullable=False)
    email : Mapped[str]= mapped_column(String(64), nullable=False, unique=True)
    text : Mapped[str] = mapped_column(Text , nullable=True)
    send_at : Mapped[datetime] = mapped_column(DateTime , server_default=func.now())

    def __repr__(self):
        return f"{self.name} contacted me"
    
class Resume(Model):
    __tablename__ = "resumes"

    id : Mapped[int] = mapped_column(primary_key=True , index=True, nullable= False , unique=True)
    header : Mapped[str] = mapped_column(Text , nullable=True)
    context : Mapped[str] = mapped_column(Text , nullable=True)
    image : Mapped[str] = mapped_column(String(64), nullable=True)
    contact : Mapped[str] =  mapped_column(String(64), nullable=True)
    archeivments : Mapped[str] = mapped_column(Text , nullable=True)
    projects : Mapped[str] = mapped_column(Text , nullable=True)
    created_at : Mapped[datetime] = mapped_column(DateTime,server_default=func.now())

    def __repr__(self):
        return f"{self.id} resume"