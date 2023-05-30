from controllers.images import categories
from fastapi import APIRouter, HTTPException, Depends
from typing import Annotated


router = APIRouter(prefix='/api/images', tags=['categories'])


@router.get('/get_folders')
def get_folders():
    return categories.get_folders()


@router.post('/category')
def get_images_from_category(category_images: Annotated[dict, Depends(categories.get_images_from_category)]):
    return category_images


@router.post("/category_favorites")
def get_category_images_with_favorite(category_favorite: Annotated[dict, Depends(categories.get_category_images_with_favorite)]):
    return category_favorite