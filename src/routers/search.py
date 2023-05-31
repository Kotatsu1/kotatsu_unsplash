from controllers.images import search
from fastapi import APIRouter, HTTPException, Depends
from typing import Annotated


router = APIRouter(prefix='/api/search', tags=['search'])


@router.post('/autocomplete')
def autocomplete_search(search: Annotated[dict, Depends(search.autocomplete_search)]):
    return search


@router.post('/images')
def search_images(search: Annotated[dict, Depends(search.search_images)]):
    return search