import os

from dotenv import load_dotenv
from pydantic import BaseModel
from fastapi import Body
from psycopg2 import Error
from fastapi import Body, Path

from ..connectionDB.dataBaseConnection import conn


class UserController: 
    def __init__(self, conn):
        self.conn = conn
        if (conn):
            print("connect db")
        else:
            print("error on dataabase:", Error)

    async def createUser(self, body = Body()):
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO testtask1 (name, surnmae, patronymic) VALUES (%s, %s, %s) RETURNING *", (body["name"], body["surname"], body["patronymic"]))
            response = await cursor.fetchone()
            conn.commit()
            conn.close()
            cursor.close()
            print(response)
            return response
        except(Error) as error:
            print(Error)
        
    async def updateUser(self, id: int = Path(), body = Body()):
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE testtask1 SET name=%s, surnmae=%s, patronymic=%s WHERE id=%s RETURNING *", (body["name"], body["surname"], body["patronymic"], id))
            response = await cursor.fetchone()
            conn.commit()
            conn.close()
            cursor.close()
            return response 
        except(Error) as error:
            print(Error)

    async def getUserById(self, id = Path()):
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM testtask1 WHERE id=%s", (id))
            response = await cursor.fetchone()
            conn.commit()
            conn.close()
            cursor.close()
            return response 
        except(Error) as error:
            print(Error)
    
    async def deleteUser(self, id = Path()):
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM testtask1 WHERE id=%s RETURNING *", (id))
            response = await cursor.fetchone()
            conn.commit()
            conn.close()
            cursor.close()
            return response 
        except(Error) as error:
            print(Error)