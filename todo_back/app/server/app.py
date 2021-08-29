from fastapi import FastAPI

from server.routes.item import router as ItemRouter
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(ItemRouter, tags=["Item"], prefix="/item")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to wonderful todo app!"}
