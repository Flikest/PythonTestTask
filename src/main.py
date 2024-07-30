from fastapi import FastAPI, Body, Path

from src.controllers.userController import UserController
from src.connectionDB.dataBaseConnection import conn


userController = UserController(conn)

app = FastAPI()

@app.post("/createuser")
def createuser(body=Body()):
    return userController.createUser(body)

@app.put("/updateuser/{id}")
def updateUser (id = Path(), body=Body()):
    return userController.updateUser(id, body)

@app.get("/getuserbyid/{id}")
def getUserById(id = Path()):
    return userController.getUserById(id)


@app.delete("/deleteuser/{id}")
def root(id = Path()): 
    return userController.deleteUser(id)