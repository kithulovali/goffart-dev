from sqlalchemy.orm import Mapped , mapped_column 
from sqlalchemy import String , DateTime 
from datetime import datetime 
from settings import Model

# Projects and Contact Models

class Project(Model):
    __tablename__ = "projects"

    id : Mapped[str] = mapped_column(primary_key=True, unique=True,index=True)
    name : Mapped[str] = mapped_column(String(64))
    description : Mapped[str] = mapped_column(String(64))
    banner : Mapped[str] = mapped_column(String(64))
    created_at : Mapped[datetime] = mapped_column(DateTime(timezone=True))

    def __repr__(self):
        return f"{self.name}"
    

class Contact(Model):
    __tablename__ = "contacts"

    id : Mapped[int] = mapped_column(primary_key=True, unique=True, index=True)
    name : Mapped[str] = mapped_column(String(64))
    email : Mapped[str] = mapped_column(String(64))
    message : Mapped[str] = mapped_column(String(64))
    send_at : Mapped[datetime] = mapped_column(DateTime(timezone=True))

    def __repr__(self):
        return f"{self.name}"