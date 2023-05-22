from controllers.images import ai
from fastapi import APIRouter, HTTPException, Depends
from typing import Annotated



router = APIRouter(prefix='/api/images/ai', tags=['ai'])


@router.post("/caption")
def image_caption(image_caption: Annotated[dict, Depends(ai.image_caption)]):
    return image_caption


@router.post("/generation")
def image_generation(image_generation: Annotated[dict, Depends(ai.image_generation)]):
    return image_generation