import os

from dotenv import load_dotenv
from fastapi import Body
from psycopg2 import Error
from fastapi import Body
import psycopg2
from dotenv import load_dotenv

import os


env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(env_path)


conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    host=os.getenv("DB_HOST")
)


class UserController: 
    def __init__(self):
        self.conn = conn
        if (conn):
            print("connect db")
        else:
            print("error on dataabase:", Error)

    async def createUser(self, body = Body()):
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO testtask1 (name, surnmae, patronymic) VALUES (%s, %s, %s) RETURNING *", (body["name"], body["surname"], body["patronymic"]))
            response = cursor.fetchone()
            conn.commit()
            conn.close()
            cursor.close()
            print(response)
            return response
        except(Error) as error:
            print(Error)
        
    async def updateUser(self, id, body = Body()):
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE testtask1 SET name=%s, surnmae=%s, patronymic=%s WHERE id=%s RETURNING *", (body["name"], body["surname"], body["patronymic"], id))
            response = cursor.fetchone()
            conn.commit()
            conn.close()
            cursor.close()
            return response 
        except(Error) as error:
            print(Error)

    async def getUserById(self, id: int):
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM testtask1 WHERE id=%s", (id,))
            response = cursor.fetchone()
            conn.commit()
            conn.close()
            cursor.close()
            return response 
        except(Error) as error:
            print(Error)
    
    async def deleteUser(self, id):
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM testtask1 WHERE id=%s RETURNING *", (id,))
            response = cursor.fetchone()
            conn.commit()
            conn.close()
            cursor.close()
            return response 
        except(Error) as error:
            print(Error)