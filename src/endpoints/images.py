from schemas.image_schemas import UploadImage
from funcs.images import get_all_images, upload_images
from fastapi import APIRouter


router = APIRouter(prefix='/api/images', tags=['search'])



@router.get('/all')
def all_images():
    return get_all_images()


@router.post('/upload')
def upload_image(request: UploadImage):
    return upload_images(request.title, request.url)
