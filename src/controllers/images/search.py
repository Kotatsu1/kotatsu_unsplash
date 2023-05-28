from fastapi import HTTPException
import cloudinary
import cloudinary.api

from dotenv import load_dotenv

load_dotenv()

# def get_file_names() -> list:
#     return list(map(lambda image: image['filename'], cloudinary.Search().execute()['resources'][::]))


# def autocomplete_search(query: str):
#     return list(filter(lambda name: name.startswith(query), get_file_names()))

def autocomplete_search(query: str):
    result = cloudinary.Search().expression(f"{query}").max_results("10").execute()
    return [image['filename'] for image in result['resources']]

