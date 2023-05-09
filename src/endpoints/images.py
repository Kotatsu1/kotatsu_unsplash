from schemas.image_schemas import UploadImage
from funcs.images import get_all_images, upload_images, get_images_from_exact_folder, get_all_folders
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
        raise HTTPException(status_code=404, detail='Error during upload')
    return 'uploaded successfully'


@router.get('/folder')
def folder_images(folder_name: str):
    return get_images_from_exact_folder(folder_name)


@router.get('/get_folders')
def get_folders():
    return get_all_folders()
