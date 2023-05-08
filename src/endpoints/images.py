from funcs.get_images import get_all_images
from fastapi import APIRouter


router = APIRouter(prefix='/api/images', tags=['search'])



@router.get('/all')
def all_images():
    return get_all_images()


