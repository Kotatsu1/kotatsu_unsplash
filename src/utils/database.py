import psycopg2
from dotenv import load_dotenv
import os
from fastapi import HTTPException

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
    

def get_user_by_token(token):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        if token is None:
            raise HTTPException(status_code=404, detail='Token is required')

        user_query = 'SELECT id FROM "User" WHERE "accessToken" = \'{}\''.format(token) 

        cursor.execute(user_query)
        user_id = cursor.fetchone()
        if user_id[0] is None:
            raise HTTPException(status_code=404, detail='User not found')

        return user_id[0]
    
    except Exception:
        return 'Could not extract user id'
    
    finally:
        cursor.close()
        connection.close()
