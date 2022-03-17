from pydantic import BaseModel
from typing import List
from enum import Enum

class resourceClass(BaseModel):
    name:str
    class Config:
        schema_extra = {
            "example": {
                "name": "Name of the resource",
            }
        }



class actions(str,Enum):
    r="read"
    w = "write"
    ex = "execute"


class rolesClass(BaseModel):
    name:str
    class objs(BaseModel):
        action : actions
        resource : resourceClass
    permissions : List[objs]
    class Config:
        schema_extra = {
            "example": {
                "name": "Name of the role",
                "permissions": ["List of the permissions"]
            }
        }

class userClass(BaseModel):
    name: str
    roles: List[str]
    class Config:
        schema_extra = {
            "example": {
                "name": "Name of the user",
                "roles": ["List of the roles"]
            }
        }