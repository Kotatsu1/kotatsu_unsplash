from dotenv import load_dotenv
load_dotenv()

import cloudinary
import cloudinary.api
import cloudinary.uploader

config = cloudinary.config(secure=True)


def get_all_images():
    return cloudinary.Search().execute()


def get_file_names():
    return list(map(lambda image: image['filename'], get_all_images()['resources'][::]))


def get_folders():
    folders = set(list(map(lambda image: image['folder'], get_all_images()['resources'][::])))
    return folders


def get_images_from_folder(folder_name, next_cursor: str | None = None):
    return cloudinary.Search().max_results("10").next_cursor(next_cursor).expression(f"folder:{folder_name}").execute()


def interactive_search(query):
    return list(filter(lambda name: name.startswith(query), get_file_names()))


def upload_image(title, url):
    return cloudinary.uploader.upload(url, public_id = title,overwrite = True,folder = 'gallery')


def get_urls(folder):
    raw_data = cloudinary.Search().expression(f"folder:{folder}").execute()
    urls = list(map(lambda image: image['url'], raw_data['resources'][::]))
    return urls



