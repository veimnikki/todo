from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.db import (
    add_item,
    delete_item,
    retrieve_item,
    retrieve_item_by_date,
    retrieve_items,
    update_item,
)
from app.server.models.item import (
    ErrorResponseModel,
    ResponseModel,
    ItemSchema,
    UpdateItemModel,
)


router = APIRouter()


@router.post("/", response_description="Item data added into the database")
async def add_item_data(item: ItemSchema = Body(...)):
    item = jsonable_encoder(item)
    new_item = await add_item(item)
    return ResponseModel(new_item, "Item added successfully.")


@router.get("/", response_description="Get items data")
async def get_items_data():
    items = await retrieve_items()
    return ResponseModel(items, "Get items data successfully.")


@router.get("/date/{date}", response_description="Get item data")
async def get_items_by_date(date: str):
    item = await retrieve_item_by_date(date)
    return ResponseModel(item, "Get item data successfully.")


@router.get("/{item_id}", response_description="Get item by date")
async def get_item_data(item_id: str):
    item = await retrieve_item(item_id)
    return ResponseModel(item, "Get item data by date successfully.")


@router.put("/{item_id}", response_description="Update item data")
async def update_item_data(item_id: str, data: UpdateItemModel = Body(...)):
    data = jsonable_encoder(data)
    item = await update_item(item_id, data)
    return ResponseModel(item, "Updated item data successfully.")


@router.delete("/{item_id}", response_description="Delete item data")
async def delete_item_data(item_id: str):
    item = await delete_item(item_id)
    return ResponseModel(item, "Delete item data successfully.")

