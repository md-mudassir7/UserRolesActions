from pymongo import MongoClient
from fastapi import FastAPI, status,HTTPException
from pydantic import BaseModel
from typing import List
from enum import Enum, EnumMeta

client = MongoClient("mongodb://localhost:27017")

db = client.assignment

user = db.user
roles = db.roles
resources = db.resources
from models import resourceClass,rolesClass,userClass,actions


app = FastAPI()



@app.get('/resources',response_model=List[resourceClass])
def get_resources():
    res = resources.find({})
    response = []
    for each in res:
        response.append(resourceClass(**each))
    if response:
        return response
    raise HTTPException(
        status_code  = 404,
        detail = f"Error"
    )

@app.post('/resources/{resource}',status_code=status.HTTP_201_CREATED)
def add_resource(value:resourceClass):
    result = resources.insert_one(value.dict())
    ack = result.acknowledged
    return {"insertion": ack}

@app.get('/roles',response_model=List[rolesClass])
def get_roles():
    res = roles.find({})
    response = []
    for each in res:
        response.append(rolesClass(**each))
    if response:
        return response
    raise HTTPException(
        status_code  = 404,
        detail = f"Error"
    )

@app.post('/roles/{role}',status_code=status.HTTP_201_CREATED)
def add_roles(value:rolesClass):
    temp = resources.find()
    response = []
    for each in temp:
        response.append(each['name'])
    temp=[]
    for each in value.permissions:
        temp.append(each.resource.name)
    flag = 1
    for i in temp:
        if i not in response:
            raise HTTPException(
                status_code  = 404,
                detail = f"Resource {i} does not exists,enter the one which exists"
            )
    if flag:
        result = roles.insert_one(value.dict())
        ack = result.acknowledged
        return {"insertion": ack}
    raise HTTPException(
        status_code  = 404,
        detail = f"Error"
    )

@app.get('/users',response_model=List[userClass])
def get_users():
    res = user.find({})
    response = []
    for each in res:
        response.append(userClass(**each))
    if response:
        return response
    raise HTTPException(
        status_code  = 404,
        detail = f"Error"
    )


@app.post('/users/{user}',status_code=status.HTTP_201_CREATED)
def add_user(value:userClass):
    temp = roles.find({})
    flag = 1
    response = []
    for each in temp:
        response.append(rolesClass(**each).name)
    print(response)
    temp=[]
    for each in value.roles:
        temp.append(each)
    print(temp)
    flag=1
    for i in temp:
        if i not in response:
            raise HTTPException(
                status_code  = 404,
                detail = f"Role with name {i} does not exists,enter the one which exists"
            )
    if flag:
        result = user.insert_one(value.dict())
        ack = result.acknowledged
        return {"insertion": ack}
    raise HTTPException(
        status_code  = 404,
        detail = f"Error"
    )


@app.get('/users/roles')
def get_users_by_role(value:str):
    print(value)
    res = user.find({})
    print(res)
    response = dict()
    s = set()
    for each in res:
        for each2 in each['roles']:
            if each2 == value:
                s.add(each['name'])
    if s:
        return s
    raise HTTPException(
        status_code  = 404,
        detail = f"No user with a role {value} exists"
    )