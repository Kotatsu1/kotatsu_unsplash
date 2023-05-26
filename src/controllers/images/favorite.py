from utils.database import get_connection, get_user_by_token
from dotenv import load_dotenv
from fastapi import HTTPException
from schemas.image_schemas import UpdateFavorite
import psycopg2

load_dotenv()


def update_favorite_image(request: UpdateFavorite):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        user_id = get_user_by_token(request.token)

        existing_image_query = (
            '''
            SELECT * 
            FROM "favoriteImages" 
            WHERE public_id = \'{}\' AND user_id = \'{}\'
            '''
        ).format(request.public_id, user_id)
        
        cursor.execute(existing_image_query)
        existing_image = cursor.fetchone()

        if existing_image is None:
            add_image_query = (
                '''
                INSERT INTO "favoriteImages" 
                (public_id, user_id) 
                VALUES (\'{}\', \'{}\')
                '''
            ).format(request.public_id, user_id)
            
            cursor.execute(add_image_query)
            connection.commit()
            return 'Image added to favorites'
        else:
            remove_image_query = (
                '''
                DELETE FROM "favoriteImages" 
                WHERE public_id = \'{}\' AND user_id = \'{}\'
                '''
            ).format(request.public_id, user_id[0])

            cursor.execute(remove_image_query)
            connection.commit()
            return 'Image removed from favorites'
        
    except psycopg2.Error as e:
        return f'Could not execute favorite image | SQL: {e}'
    
    finally:
        cursor.close()
        connection.close()


def user_favorive_images(token: str):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        user_id = get_user_by_token(token)

        favorite_images_query = (
            '''
            SELECT public_id 
            FROM "favoriteImages" 
            WHERE user_id = \'{}\'
            '''
        ).format(user_id)
        
        cursor.execute(favorite_images_query)
        rows = cursor.fetchall()
        all_favorites = [row[0] for row in rows]

        if all_favorites is None:
            raise HTTPException(status_code=404, detail='No favorite images found')
        return all_favorites
    
    except psycopg2.Error as e:
        return f'Could not fetch user favorite images | SQL: {e}'
    
    finally:
        cursor.close()
        connection.close()
