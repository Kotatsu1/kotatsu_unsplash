from pydantic import BaseModel


class UploadImage(BaseModel):
    title: str
    url: str


class Favorite(BaseModel):
    public_id: str
    token: str