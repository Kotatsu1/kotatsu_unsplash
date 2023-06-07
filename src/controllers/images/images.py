from fastapi import HTTPException
import cloudinary
import cloudinary.api
import cloudinary.uploader
from dotenv import load_dotenv
from controllers.images import favorite
from schemas.image_schemas import FetchAllFavorites, FetchImages, UploadImage


load_dotenv()

config = cloudinary.config(secure=True)


def get_images_from_all_categories(request: FetchImages) -> dict:
    images = cloudinary.Search().max_results("50").next_cursor(request.next_cursor).execute()
    images.update({'page_preview': 'http://45.87.246.48:8000/page_preview/editorial.avif'})
    return images
        

def upload_image(request: UploadImage):
    try:
        cloudinary.uploader.upload(request.url, public_id = request.title, overwrite = True, folder = request.folder)
        return 'Image uploaded successfully'
    except Exception:
        raise HTTPException(status_code=500, detail='Could not upload image')


def get_all_images_with_favorite(request: FetchAllFavorites):
    all_images = cloudinary.Search().max_results("50").next_cursor(request.next_cursor).execute()
    all_images.update({'page_preview': 'http://45.87.246.48:8000/page_preview/editorial.avif'})
    favorite_images = favorite.user_favorive_images(request.token)

    def mark_favorite(image):
        if image['public_id'] in favorite_images:
            image['favorite'] = True
        else:
            image['favorite'] = False
        return image

    all_images['resources'] = list(map(mark_favorite, all_images['resources']))
    return all_images


