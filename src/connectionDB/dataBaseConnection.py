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