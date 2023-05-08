from dotenv import load_dotenv
load_dotenv()

import cloudinary
import cloudinary.api

config = cloudinary.config(secure=True)


def get_all_images():
    return cloudinary.Search().execute()
images = get_all_images()

def get_file_names(all_images):
    response = all_images
    return list(map(lambda image: image['filename'], response['resources'][::]))


def interactive_search(query):
    return list(filter(lambda name: name.startswith(query), get_file_names(images)))