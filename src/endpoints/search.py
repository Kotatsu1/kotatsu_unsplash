from fastapi import APIRouter
from funcs import images
from schemas.search_schemas import Search

router = APIRouter(prefix='/api/images', tags=['search'])

@router.post("/search")
def search(q: Search):
    return {'search': images.interactive_search(q.query)}

