from controllers.images import collections
from fastapi import APIRouter, Depends
from typing import Annotated

router = APIRouter(prefix='/api/collections', tags=['collections'])


@router.post("/create")
def create_collection(result: Annotated[dict, Depends(collections.create_collection)]):
    return result


@router.post('/user-collections')
def get_user_collection(result: Annotated[dict, Depends(collections.get_user_collection)]):
    return result


@router.post('/delete')
def delete_collection(result: Annotated[dict, Depends(collections.delete_collection)]):
    return result


@router.put('/update')
def update_collection_info(result: Annotated[dict, Depends(collections.update_collection_info)]):
    return result


@router.post('/add-images')
def add_images_to_collection(result: Annotated[dict, Depends(collections.add_images_to_collection)]):
    return result


@router.post('/delete-images')
def delete_images_from_collection(result: Annotated[dict, Depends(collections.delete_images_from_collection)]):
    return result


@router.post('/collection-content')
def get_collection_content(result: Annotated[dict, Depends(collections.get_images_from_collection)]):
    return result


@router.post('/collection-content-favorite')
def get_collection_content_favorite(result: Annotated[dict, Depends(collections.get_images_from_collection_with_favorite)]):
    return result