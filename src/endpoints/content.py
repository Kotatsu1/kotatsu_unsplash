
from fastapi import APIRouter


router = APIRouter(prefix='/api/content', tags=['content'])



@router.get('/')
def all_images():
    return ''


