from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import images, ai
import uvicorn


app = FastAPI(title='Unsplash API',)


app.include_router(images.router)
app.include_router(ai.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


if __name__ == "__main__":
   uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)