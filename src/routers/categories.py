from controllers.images import categories
from fastapi import APIRouter, HTTPException, Depends
from typing import Annotated


router = APIRouter(prefix='/api/categories', tags=['categories'])


@router.get('/all_categories')
def get_categories():
    return categories.get_categories()


@router.post('/all_images')
def get_images_from_category(category_images: Annotated[dict, Depends(categories.get_images_from_category)]):
    return category_images


@router.post("/favorite_images")
def get_category_images_with_favorite(category_favorite: Annotated[dict, Depends(categories.get_category_images_with_favorite)]):
    return category_favorite