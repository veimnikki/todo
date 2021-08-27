from fastapi import FastAPI

from app.server.routes.item import router as ItemRouter

app = FastAPI()

app.include_router(ItemRouter, tags=["Item"], prefix="/item")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to wonderful todo app!"}
