from pydantic import BaseModel


class CreateCollection(BaseModel):
    token: str
    title: str
    description: str