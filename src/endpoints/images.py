from schemas.image_schemas import UploadImage
from funcs.images import get_all_images, upload_images
from fastapi import APIRouter, HTTPException


router = APIRouter(prefix='/api/images', tags=['search'])



@router.get('/all')
def all_images():
    return get_all_images()


@router.post('/upload')
def upload_image(request: UploadImage):
    try:
        upload_images(request.title, request.url)
    except Exception:
        raise HTTPException(status_code=400, detail='Error during upload')
    return 'uploaded successfully'
