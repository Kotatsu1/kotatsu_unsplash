from fastapi import APIRouter
from controllers import images


router = APIRouter(prefix='/api/images', tags=['search'])

@router.post("/search")
def autocomplete_search(query: str):
    return {'search': images.autocomplete_search(query)}

