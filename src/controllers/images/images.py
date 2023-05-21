from fastapi import HTTPException
import cloudinary
import cloudinary.api
import cloudinary.uploader
from utils import database
import psycopg2
from dotenv import load_dotenv
import replicate

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


def image_caption(image_url):
    caption = replicate.run(
            "salesforce/blip:2e1dddc8621f72155f24cf2e0adbde548458d3cab9f00c0139eea840d0ac4746",
            input={"image": image_url},
        )
    return caption

