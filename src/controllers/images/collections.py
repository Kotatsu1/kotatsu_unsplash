from fastapi import HTTPException
from schemas.collections_schemas import CreateCollection, FetchUserCollections, DeleteCollection, UpdateCollection, AddImages, DeleteImages
from utils.database import get_connection, get_user_by_token
import psycopg2

def create_collection(request: CreateCollection):
    token = request.token
    title = request.title
    description = request.description
    try:
        connection = get_connection()
        cursor = connection.cursor()

        user_id = get_user_by_token(token)

        collection_query = 'INSERT INTO collections (title, description, fk_user_id) VALUES (\'{}\', \'{}\', \'{}\')'.format(title, description, user_id)

        cursor.execute(collection_query)
        connection.commit()

        return 'Collection created successfully'
    except psycopg2.Error as e:
        return f'Could not create collection | SQL: {e}'
    
    finally:
        cursor.close()
        connection.close()


def get_user_collection(request: FetchUserCollections):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        collection_query = 'SELECT json_agg(row_to_json(t)) FROM (SELECT * FROM collections WHERE fk_user_id = \'{}\') t'.format(request.user_id)
        
        cursor.execute(collection_query)
        collections = cursor.fetchall()

        return collections[0][0]
    except psycopg2.Error as e:
        return f'Could not get collections | SQL: {e}'
    
    finally:
        cursor.close()
        connection.close()


def delete_collection(request: DeleteCollection):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        user_id = get_user_by_token(request.token)

        collection_query = 'DELETE FROM collections WHERE collection_id = \'{}\' AND fk_user_id = \'{}\''.format(request.id, user_id)

        cursor.execute(collection_query)
        connection.commit()

        return 'Collection deleted successfully'
    except psycopg2.Error as e:
        return f'Could not delete collection | SQL: {e}'
    
    finally:
        cursor.close()
        connection.close()


def update_collection_info(request: UpdateCollection):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        user_id = get_user_by_token(request.token)

        collection_query = 'UPDATE collections SET title = \'{}\', description = \'{}\' WHERE collection_id = \'{}\' AND fk_user_id = \'{}\''.format(request.title, request.description, request.id, user_id)

        cursor.execute(collection_query)
        connection.commit()

        return 'Collection info updated successfully'
    except psycopg2.Error as e:
        return f'Could not update collection info | SQL: {e}'
    
    finally:
        cursor.close()
        connection.close()


def add_images_to_collection(request: AddImages):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        user_id = get_user_by_token(request.token)

        check_collection_query = 'SELECT collection_id FROM collections WHERE fk_user_id = \'{}\''.format(user_id)
        cursor.execute(check_collection_query)
        valid_collections_list = cursor.fetchall()
        valid_collections_list = [i[0] for i in valid_collections_list]

        if request.collection_id in valid_collections_list:
            collection_query = 'INSERT INTO collection_content (public_id, fk_collection_id) VALUES (\'{}\', \'{}\')'.format(request.public_id, request.collection_id)

            cursor.execute(collection_query)
            connection.commit()

            return 'Image added successfully'
        else:
            raise HTTPException(status_code=404, detail="You cannot manage this collection")
        return valid_collections_list
    except psycopg2.Error as e:
        return f'Could not add image to collection, | SQL: {e}'
    
    finally:
        cursor.close()
        connection.close()


def delete_images_from_collection(request: DeleteImages):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        user_id = get_user_by_token(request.token)

        check_collection_query = 'SELECT collection_id FROM collections WHERE fk_user_id = \'{}\''.format(user_id)
        cursor.execute(check_collection_query)
        valid_collections_list = cursor.fetchall()
        valid_collections_list = [i[0] for i in valid_collections_list]

        if request.collection_id in valid_collections_list:
            collection_query = 'DELETE FROM collection_content WHERE public_id = \'{}\' AND fk_collection_id = \'{}\''.format(request.public_id, request.collection_id)

            cursor.execute(collection_query)
            connection.commit()

            return 'Image deleted successfully'
        else:
            raise HTTPException(status_code=404, detail="You cannot manage this collection")
        return valid_collections_list
    except psycopg2.Error as e:
        return f'Could not delete image from collection, | SQL: {e}'
    
    finally:
        cursor.close()
        connection.close()