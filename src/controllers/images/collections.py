from fastapi import HTTPException
from schemas.collections_schemas import CreateCollection
from utils.database import get_connection

def create_collection(request: CreateCollection):
    token = request.token
    title = request.title
    description = request.description
    try:
        connection = get_connection()
        cursor = connection.cursor()

        if token is None:
            raise HTTPException(status_code=404, detail='Token is required')

        user_query = 'SELECT id FROM "User" WHERE "accessToken" = \'{}\''.format(token) 

        cursor.execute(user_query)
        user_id = cursor.fetchone()
        if user_id is None:
            raise HTTPException(status_code=404, detail='User not found')

        collection_query = 'INSERT INTO "collections" (title, description, owner) VALUES (\'{}\', \'{}\', \'{}\')'.format(title, description, user_id[0])

        cursor.execute(collection_query)
        connection.commit()

        return 'Collection created successfully'
    except Exception:
        return 'Could not create collection'
    
    finally:
        cursor.close()
        connection.close()
