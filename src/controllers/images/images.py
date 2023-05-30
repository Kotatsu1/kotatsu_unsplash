from fastapi import HTTPException
import cloudinary
import cloudinary.api
import cloudinary.uploader
from dotenv import load_dotenv
from controllers.images import favorite
from schemas.image_schemas import FetchAllFavorites, FetchImages, UploadImage, FetchFromCategory, FetchCategoryFavorites


load_dotenv()

config = cloudinary.config(secure=True)


def get_images_from_all_categories(request: FetchImages) -> dict:
    return cloudinary.Search().max_results("50").next_cursor(request.next_cursor).execute()
        

def get_folders() -> dict:
    return cloudinary.api.root_folders()


def get_images_from_category(request: FetchFromCategory):
    try:
        return cloudinary.Search().max_results("50").next_cursor(request.next_cursor).expression(f"folder:{request.folder}").execute()
    except Exception:
        raise HTTPException(status_code=404, detail='Cound not get images from category')

def upload_image(request: UploadImage):
    try:
        cloudinary.uploader.upload(request.url, public_id = request.title, overwrite = True, folder = request.folder)
        return 'Image uploaded successfully'
    except Exception:
        raise HTTPException(status_code=500, detail='Could not upload image')


def get_all_images_with_favorite(request: FetchAllFavorites):
    all_images = cloudinary.Search().max_results("50").next_cursor(request.next_cursor).execute()
    favorite_images = favorite.user_favorive_images(request.token)

    def mark_favorite(image):
        if image['public_id'] in favorite_images:
            image['favorite'] = True
        else:
            image['favorite'] = False
        return image


    all_images['resources'] = list(map(mark_favorite, all_images['resources']))

    return all_images


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

