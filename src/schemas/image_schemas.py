from pydantic import BaseModel


class UploadImage(BaseModel):
    title: str
    url: str


class UpdateFavorite(BaseModel):
    public_id: str
    token: str


class FetchFavorites(BaseModel):
    token: str
    class Config():
        orm_mode = True
