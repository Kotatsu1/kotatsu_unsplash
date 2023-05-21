from utils import database
import psycopg2
from dotenv import load_dotenv
from fastapi import HTTPException
from schemas.image_schemas import Favorite

load_dotenv()


def favorite_image(request: Favorite):
    public_id, token = request.public_id, request.token

    connection = database.get_connection()
    cursor = connection.cursor()
    try:
        if token and public_id is None:
            raise HTTPException(status_code=404, detail='Token and public_id is required')

        user_query = 'SELECT id FROM "User" WHERE "accessToken" = \'{}\''.format(token) 

        cursor.execute(user_query)
        user_id = cursor.fetchone()

        if user_id is None:
            raise HTTPException(status_code=404, detail='User not found')

        existing_image_query = 'SELECT * FROM "favoriteImages" WHERE public_id = \'{}\' AND user_id = \'{}\''.format(public_id, user_id[0])

        cursor.execute(existing_image_query)
        existing_image = cursor.fetchone()


        if existing_image is None:
            add_image_query = 'INSERT INTO "favoriteImages" (public_id, user_id) VALUES ({}, \'{}\')'.format(public_id, user_id[0])
            cursor.execute(add_image_query)
            connection.commit()
            cursor.close()
            connection.close()
            return 'Image added to favorites'

        else:
            remove_image_query = 'DELETE FROM "favoriteImages" WHERE public_id = \'{}\' AND user_id = \'{}\''.format(public_id, user_id[0])
            cursor.execute(remove_image_query)
            connection.commit()
            cursor.close()
            connection.close()
            return 'Image removed from favorites'
        
    except psycopg2.Error as e:
        raise HTTPException(status_code=500, detail='Failed to favorite image' + ' SQL DETAIL: ' + str(e))
