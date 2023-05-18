from dotenv import load_dotenv
load_dotenv()

import cloudinary
import cloudinary.api
import cloudinary.uploader

from db import database


config = cloudinary.config(secure=True)



def get_images_from_all_categories():
    return cloudinary.Search().execute()


def get_file_names():
    return list(map(lambda image: image['filename'], get_images_from_all_categories()['resources'][::]))


def get_all_categories():
    folders = set(list(map(lambda image: image['folder'],get_images_from_all_categories()['resources'][::])))
    return folders


def get_images_from_category(folder_name, next_cursor: str | None = None):
    return cloudinary.Search().max_results("30").next_cursor(next_cursor).expression(f"folder:{folder_name}").execute()


def autocomplete_search(query: str):
    return list(filter(lambda name: name.startswith(query), get_file_names()))


def upload_image(title, url):
    return cloudinary.uploader.upload(url, public_id = title, overwrite = True, folder = 'gallery')


# def add_favorite_image_to_db(image_url: str, user_email: str):
#     connection = database.get_connection()
#     query = "INSERT INTO favoriteImages (user_email, image_url) VALUES ('{}', '{}')".format(user_email, image_url)

#     cursor = connection.cursor()
#     cursor.execute(query)
#     connection.commit()
#     cursor.close()
#     connection.close()

def get_all_users():
    connection = database.get_connection()

    cursor = connection.cursor()
    cursor.execute('SELECT * FROM "User"')
    users = cursor.fetchall()
    cursor.close()
    connection.close()

    return users

