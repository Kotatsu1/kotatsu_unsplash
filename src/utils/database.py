import psycopg2
from dotenv import load_dotenv
import os
from fastapi import HTTPException
from psycopg2.extensions import connection

load_dotenv()

def get_connection() -> connection:
    try:
        connection = psycopg2.connect(
            database=os.getenv("DB_DATABASE"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST")
        )
        return connection
    
    except psycopg2.Error as e:
        return f'Could not connect to database | SQL: {e}'
    

def get_user_by_token(token: str) -> str:
    try:
        connection = get_connection()
        cursor = connection.cursor()

        if token is None:
            raise HTTPException(status_code=404, detail='Token is required')

        user_query = (
            '''
            SELECT id 
            FROM "User" WHERE 
            "accessToken" = \'{}\'
            '''
        ).format(token) 
        
        cursor.execute(user_query)
        user_id = cursor.fetchone()
        if user_id[0] is None:
            raise HTTPException(status_code=404, detail='User not found')

        return user_id[0]
    
    except psycopg2.Error as e:
        return f'Could not extract user_id | SQL: {e}'
    
    finally:
        cursor.close()
        connection.close()
