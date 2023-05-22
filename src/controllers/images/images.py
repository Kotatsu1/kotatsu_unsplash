from fastapi import HTTPException
import cloudinary
import cloudinary.api
import cloudinary.uploader
from dotenv import load_dotenv
from controllers.images import favorite

load_dotenv()

config = cloudinary.config(secure=True)


def get_images_from_all_categories():
    return cloudinary.Search().execute()


def get_file_names():
    return list(map(lambda image: image['filename'], get_images_from_all_categories()['resources'][::]))


def get_all_categories():
    folders = set(list(map(lambda image: image['folder'], get_images_from_all_categories()['resources'][::])))
    return folders


def get_images_from_category(folder_name, next_cursor: str | None = None):
    return cloudinary.Search().max_results("30").next_cursor(next_cursor).expression(f"folder:{folder_name}").execute()


def autocomplete_search(query: str):
    return list(filter(lambda name: name.startswith(query), get_file_names()))


def upload_image(title, url):
    return cloudinary.uploader.upload(url, public_id = title, overwrite = True, folder = 'gallery')


def get_all_images_with_favorite(token: str,):
    all_images = get_images_from_all_categories()
    favorite_images = favorite.user_favorive_images(token)

    all_images['resources'] = list(map(
        lambda image: {**image, 'favorite': True}  if image['public_id'] in favorite_images else {**image, 'favorite': False},
        all_images['resources']
    ))

    return all_images

