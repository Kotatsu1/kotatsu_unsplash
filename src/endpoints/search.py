from fastapi import APIRouter
from funcs.get_images import interactive_search, get_all_images
from schemas.search_schemas import Search

router = APIRouter(prefix='/api', tags=['search'])

@router.post("/interactive")
def search(q: Search):
    return {'search': interactive_search(q.query)}

@router.get('/images')
def all_images():
    return get_all_images()