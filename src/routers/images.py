from schemas.image_schemas import UploadImage
from controllers.images import images, favorite
from fastapi import APIRouter, HTTPException, Depends
import requests
from io import BytesIO
from typing import Annotated



router = APIRouter(prefix='/api/images', tags=['images'])



@router.get('/all')
def get_images_from_all_categories():
    return images.get_images_from_all_categories()


@router.post('/upload', description='For now in Gallery folder')
def upload_image(request: UploadImage):
    try:
        response = images.upload_image(request.title, request.url)
    except Exception:
        raise HTTPException(status_code=404, detail='Error during upload')
    return response


@router.get('/category')
def get_images_from_category(folder_name: str, next_cursor: str | None = None):
    print(folder_name)
    return images.get_images_from_category(folder_name, next_cursor)


@router.get('/get_folders')
def get_all_categories():
    return images.get_all_categories()


@router.post("/search")
def autocomplete_search(query: str):
    return {'search': images.autocomplete_search(query)}


@router.post("/caption")
def image_caption(image_caption: Annotated[dict, Depends(images.image_caption)]):
    return image_caption


@router.post("/favorite")
def favorite_image(favorite: Annotated[dict, Depends(favorite.update_favorite_image)]):
    return favorite


@router.get("/user_favorites")
def get_all_images_with_favorite(user_favorite: Annotated[dict, Depends(images.get_all_images_with_favorite)]):
    return user_favorite