from controllers.images import collections
from fastapi import APIRouter, Depends
from typing import Annotated

router = APIRouter(prefix='/api/collections', tags=['collections'])


@router.post("/create")
def create_collection(result: Annotated[dict, Depends(collections.create_collection)]):
    return result


@router.post('/user_collections')
def get_user_collection(result: Annotated[dict, Depends(collections.get_user_collection)]):
    return result


@router.post('/delete')
def delete_collection(result: Annotated[dict, Depends(collections.delete_collection)]):
    return result


@router.put('/update')
def update_collection_info(result: Annotated[dict, Depends(collections.update_collection_info)]):
    return result


@router.post('/add_images')
def add_images_to_collection(result: Annotated[dict, Depends(collections.add_images_to_collection)]):
    return result


@router.post('/delete_images')
def delete_images_from_collection(result: Annotated[dict, Depends(collections.delete_images_from_collection)]):
    return result