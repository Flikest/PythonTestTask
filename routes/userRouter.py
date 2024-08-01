from fastapi import APIRouter, Body, Path

from controllers.userController import UserController


userController = UserController()

router = APIRouter()

@router.post("/createuser")
async def createuser(body=Body()):
    return await userController.createUser(body)

@router.put("/updateuser/{id}")
async def updateUser (id: int, body=Body()):
    return await userController.updateUser(id, body)

@router.get("/getuserbyid/{id}")
async def getUserById(id: int):
    return await userController.getUserById(id)


@router.delete("/deleteuser/{id}")
async def root(id: int): 
    return await userController.deleteUser(id)