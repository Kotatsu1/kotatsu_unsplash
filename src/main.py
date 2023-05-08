from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from endpoints import search
import uvicorn

app = FastAPI()


# hello world

app.include_router(search.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


if __name__ == "__main__":
   uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)