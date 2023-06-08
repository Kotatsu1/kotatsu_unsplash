from fastapi import HTTPException
import cloudinary
import cloudinary.api
import cloudinary.uploader
from dotenv import load_dotenv
from controllers.images import favorite
from schemas.image_schemas import FetchAllFavorites, FetchImages, UploadImage
from utils.favorites import mark_favorite
from utils.page_preview import add_page_preview


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
    added_preview = add_page_preview(all_images, 'editorial')
    resources = added_preview['resources']
    favorite_images = favorite.user_favorive_images(request.token)


    updated_resources = list(map(lambda image: mark_favorite(image, favorite_images), resources))

    return {**added_preview, 'resources': updated_resources}


