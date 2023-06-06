from controllers.cms import cms
from fastapi import APIRouter, HTTPException, Depends
from typing import Annotated


router = APIRouter(prefix='/api/cms', tags=['cms'])


@router.get('/all-images')
def get_images_from_category(test: Annotated[dict, Depends(cms.cftest)]):
    return test
