from controllers.images import collections
from fastapi import APIRouter, Depends
from typing import Annotated

router = APIRouter(prefix='/api/collections', tags=['collections'])


@router.post("/create")
def create_collection(result: Annotated[dict, Depends(collections.create_collection)]):
    return result

