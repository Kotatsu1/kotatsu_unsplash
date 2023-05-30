from schemas.image_schemas import UploadImage
from controllers.images import images, favorite
from fastapi import APIRouter, HTTPException, Depends
from typing import Annotated


router = APIRouter(prefix='/api/images', tags=['images'])


@router.post('/all')
def get_images_from_all_categories(all_images: Annotated[dict, Depends(images.get_images_from_all_categories)]):
    return all_images


@router.post('/upload', description='For now in Gallery folder')
def upload_image(upload_image: Annotated[dict, Depends(images.upload_image)]):
    return upload_image






@router.post("/search")
def autocomplete_search(query: str):
    return {'search': images.autocomplete_search(query)}


@router.post("/update_favorite")
def update_favorite_image(updated_favorite: Annotated[dict, Depends(favorite.update_favorite_image)]):
    return updated_favorite


@router.post("/all_favorites")
def get_all_images_with_favorite(user_favorite: Annotated[dict, Depends(images.get_all_images_with_favorite)]):
    return user_favorite


