from datetime import date, datetime

import motor.motor_asyncio
from bson.objectid import ObjectId


MONGO_DETAILS = 'mongodb+srv://todo_admin:veimnikki69@cluster0.bmyul.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.todo
items_collection = database.get_collection("items_collection")


# helpers
def item_helper(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "title": item["title"],
        "date": item["date"],
        "completed": item["completed"],
        "pinned": item["pinned"],
    }


# Retrieve all items present in the database
async def retrieve_items():
    items = []
    async for item in items_collection.find():
        items.append(item_helper(item))
    return items


# Add a new item into to the database
async def add_item(item_data: dict) -> dict:
    item = await items_collection.insert_one(item_data)
    new_item = await items_collection.find_one({"_id": item.inserted_id})
    return item_helper(new_item)


# Retrieve a item with a matching ID
async def retrieve_item(id: str) -> dict:
    item = await items_collection.find_one({"_id": ObjectId(id)})
    if item:
        return item_helper(item)


# Retrieve a item with a date
async def retrieve_item_by_date(date: str):
    items = []
    async for item in items_collection.find():
        items.append(item_helper(item))
    return list(filter(lambda item: (item['date'] == date) , items))


# Update a item with a matching ID
async def update_item(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    item = await items_collection.find_one({"_id": ObjectId(id)})
    if item:
        updated_item = await items_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_item:
            return True
        return False


# Delete a item from the database
async def delete_item(id: str):
    item = await items_collection.find_one({"_id": ObjectId(id)})
    if item:
        await items_collection.delete_one({"_id": ObjectId(id)})
        return True