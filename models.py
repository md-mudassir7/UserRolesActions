from pydantic import BaseModel
from typing import List
from enum import Enum

class resourceClass(BaseModel):
    name:str


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

class userClass(BaseModel):
    name: str
    roles: List[str]