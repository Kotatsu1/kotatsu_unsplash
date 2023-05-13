from schemas.image_schemas import UploadImage
from controllers import images
from fastapi import APIRouter, HTTPException


router = APIRouter(prefix='/api/images', tags=['images'])



@router.get('/all')
def get_images_from_all_categories():
    return images.get_images_from_all_categories()


@router.post('/upload', description='For now in Gallery folder')
def upload_image(request: UploadImage):
    try:
        response = images.upload_image(request.title, request.url)
    except Exception:
        raise HTTPException(status_code=404, detail='Error during upload')
    return response


@router.get('/category')
def get_images_from_category(folder_name: str, next_cursor: str | None = None):
    print(folder_name)
    return images.get_images_from_category(folder_name, next_cursor)


@router.get('/get_folders')
def get_all_categories():
    return images.get_all_categories()


@router.post("/search")
def autocomplete_search(query: str):
    return {'search': images.autocomplete_search(query)}

