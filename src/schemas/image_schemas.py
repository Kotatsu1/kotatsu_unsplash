from pydantic import BaseModel


class UploadImage(BaseModel):
    title: str
    url: str
