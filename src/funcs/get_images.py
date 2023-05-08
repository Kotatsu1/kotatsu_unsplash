from dotenv import load_dotenv
load_dotenv()

import cloudinary
import cloudinary.api

config = cloudinary.config(secure=True)



def get_names_from_cloudinary():
    response = cloudinary.Search().execute()

    return list(map(lambda image: image['filename'], response['resources'][::]))


def get_all_images():
    return cloudinary.Search().execute()


def interactive_search(query):
    return [element for element in get_names_from_cloudinary() if element.startswith(query)]
