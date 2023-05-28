from controllers.images import search
from fastapi import APIRouter, HTTPException, Depends
from typing import Annotated


router = APIRouter(prefix='/api/search', tags=['search'])


@router.post('/all')
def autocomplete_search(search: Annotated[dict, Depends(search.autocomplete_search)]):
    return search
