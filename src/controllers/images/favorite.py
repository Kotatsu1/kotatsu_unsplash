from utils.database import get_connection
from dotenv import load_dotenv
from fastapi import HTTPException
from schemas.image_schemas import UpdateFavorite

load_dotenv()


def update_favorite_image(request: UpdateFavorite):
    public_id, token = request.public_id, request.token
    try:
        connection = get_connection()
        cursor = connection.cursor()

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
            add_image_query = 'INSERT INTO "favoriteImages" (public_id, user_id) VALUES (\'{}\', \'{}\')'.format(public_id, user_id[0])
            cursor.execute(add_image_query)
            connection.commit()
            return 'Image added to favorites'
        else:
            remove_image_query = 'DELETE FROM "favoriteImages" WHERE public_id = \'{}\' AND user_id = \'{}\''.format(public_id, user_id[0])
            cursor.execute(remove_image_query)
            connection.commit()
            return 'Image removed from favorites'
        
    except Exception:
        return 'Could not execute favorite image'
    
    finally:
        cursor.close()
        connection.close()



def user_favorive_images(token: str):
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

        favorite_images_query = 'SELECT public_id FROM "favoriteImages" WHERE user_id = \'{}\''.format(user_id[0])

        cursor.execute(favorite_images_query)
        rows = cursor.fetchall()
        all_favorites = [row[0] for row in rows]

        if all_favorites is None:
            raise HTTPException(status_code=404, detail='No favorite images found')
        return all_favorites
    
    except Exception:
        return 'Could not fetch user favorite images'
    
    finally:
        cursor.close()
        connection.close()
