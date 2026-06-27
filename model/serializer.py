from pydantic import BaseModel , Field ,EmailStr
from typing import Optional , List 

class Create_Project(BaseModel):
    name :str = Field(max_length=200)
    description : str = Field(max_length=300)
    source : List[str]
    banner : Optional[str] 

class Update_Project(BaseModel):
    name :str = Field(max_length=200)
    description : str = Field(max_length=300)
    source : List[str]
    banner : Optional[str] 

class Send_Message(BaseModel):
    name :str = Field(max_length=30)
    email : EmailStr
    message : str = Field(max_length=200)

