from pydantic import BaseModel


class CreateCollection(BaseModel):
    token: str
    title: str
    description: str


class UpdateCollection(BaseModel):
    token: str
    id: int
    title: str
    description: str


class FetchUserCollections(BaseModel):
    user_id: str


class DeleteCollection(BaseModel):
    id: int
    token: str


class AddImages(BaseModel):
    token: str
    public_id: str
    collection_id: int


class DeleteImages(BaseModel):
    token: str
    public_id: str
    collection_id: int

