import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def get_connection():
    connection = psycopg2.connect(
        database=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST")
    )
    return connection
