from fastapi import HTTPException
import cloudinary
import cloudinary.api
from dotenv import load_dotenv
from controllers.images import favorite
from schemas.image_schemas import FetchFromCategory, FetchCategoryFavorites


load_dotenv()

config = cloudinary.config(secure=True)



def get_folders() -> dict:
    return cloudinary.api.root_folders()


def get_images_from_category(request: FetchFromCategory):
    try:
        return cloudinary.Search().max_results("50").next_cursor(request.next_cursor).expression(f"folder:{request.folder}").execute()
    except Exception:
        raise HTTPException(status_code=404, detail='Cound not get images from category')


def get_category_images_with_favorite(request: FetchCategoryFavorites):
    all_images = cloudinary.Search().max_results("50").next_cursor(request.next_cursor).expression(f"folder:{request.category}").execute()
    favorite_images = favorite.user_favorive_images(request.token)

    def mark_favorite(image):
        if image['public_id'] in favorite_images:
            image['favorite'] = True
        else:
            image['favorite'] = False
        return image


    all_images['resources'] = list(map(mark_favorite, all_images['resources']))

    return all_images
