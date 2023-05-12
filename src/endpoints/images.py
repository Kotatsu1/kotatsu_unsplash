from schemas.image_schemas import UploadImage
from funcs import images
from fastapi import APIRouter, HTTPException


router = APIRouter(prefix='/api/images', tags=['search'])



@router.get('/all')
def get_all_images():
    return images.get_all_images()


@router.post('/upload')
def upload_image(request: UploadImage):
    try:
        images.upload_image(request.title, request.url)
    except Exception:
        raise HTTPException(status_code=404, detail='Error during upload')
    return 'uploaded successfully'


@router.get('/folder')
def folder_images(folder_name: str):
    return images.get_images_from_folder(folder_name)


@router.get('/get_folders')
def get_folders():
    return images.get_folders()


@router.get('/get_urls')
def get_urls(folder: str):
    return images.get_urls(folder)