from fastapi import APIRouter
from funcs.get_images import interactive_search, get_full_json
from schemas.search_schemas import Search

router = APIRouter()

@router.post("/search")
def search(q: Search):
    return {'search': interactive_search(q.query)}

@router.post('/full_json')
def full_json():
    return get_full_json()