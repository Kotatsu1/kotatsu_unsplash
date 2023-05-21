import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def get_connection():
    try:
        connection = psycopg2.connect(
            database=os.getenv("DB_DATABASE"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST")
        )
        return connection
    except Exception:
        return 'Could not connect to database'