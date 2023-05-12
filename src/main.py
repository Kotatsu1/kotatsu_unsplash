from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from endpoints import search, images, content
import uvicorn
from db.database import engine
from db import models

app = FastAPI()


# hello world

app.include_router(search.router)
app.include_router(images.router)
app.include_router(content.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


models.Base.metadata.create_all(engine)


if __name__ == "__main__":
   uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)