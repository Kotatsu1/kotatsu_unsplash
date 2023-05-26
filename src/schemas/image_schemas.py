from pydantic import BaseModel


class FetchImages(BaseModel):
    next_cursor: str


class FetchFromCategory(BaseModel):
    folder: str
    next_cursor: str


class UploadImage(BaseModel):
    folder: str
    title: str
    url: str


class UpdateFavorite(BaseModel):
    public_id: str
    token: str


class FetchFavorites(BaseModel):
    token: str
    next_cursor: str