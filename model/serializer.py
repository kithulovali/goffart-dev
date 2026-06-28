from pydantic import BaseModel , Field ,EmailStr
from typing import Optional , List 

class CreateProject(BaseModel):
    name :str = Field(max_length=200)
    description : str = Field(max_length=300)
    source :  Optional[List[str]]
    banner : Optional[str] 

class UpdateProject(BaseModel):
    name :str = Field(max_length=200)
    description : str = Field(max_length=300)
    source : Optional[List[str]]
    banner : Optional[str] 

class ProjectResponse(BaseModel):
    name : str 
    description :str 
    source : str 
    banner : str 
class SendMessage(BaseModel):
    name :str = Field(max_length=30)
    email : EmailStr
    message :Optional[str] = Field(max_length=200) 



