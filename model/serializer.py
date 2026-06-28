from pydantic import BaseModel , Field , EmailStr 
from typing import Optional 

class CreateProject(BaseModel):
    name : str = Field(max_length=50)
    description : Optional[str] = Field(max_length=200)
    banner : Optional[str]
    source : Optional[str]


class UpdateProject(BaseModel):
    name : str = Field(max_length=50)
    description : Optional[str] = Field(max_length=200)
    banner : Optional[str]
    source : Optional[str]

class ReadProject(BaseModel):
    name : str 
    description :str
    banner : str
    source : str 

class SendFeedBack(BaseModel):
    name : str 
    email : EmailStr
    text : Optional[str]

class ReadFeedBack(BaseModel):
    name : str 
    email : str
    text : str 

class CreateResume(BaseModel):
    header : Optional[str]
    context : Optional[str]
    image : Optional[str]
    contact : Optional[str]
    archeivments :Optional[str]
    projects : Optional[str]


class UpdateResume(BaseModel):
    header : Optional[str]
    context : Optional[str]
    image : Optional[str]
    contact : Optional[str]
    archeivments :Optional[str]
    projects : Optional[str]


class ReadResume(BaseModel):
    header : str
    context : str
    image : str
    contact : str
    archeivments :str
    projects : str