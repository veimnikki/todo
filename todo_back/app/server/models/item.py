from pydantic import BaseModel, Field


class ItemSchema(BaseModel):
    title: str = Field(...)
    date: str = Field(...)
    completed: bool = Field(...)
    pinned: bool = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "title": "Buy a present",
                "date": "27-02-2022",
                "completed": True,
                "pinned": False
            }
        }


class UpdateItemModel(BaseModel):
    title: str = Field(...)
    date: str = Field(...)
    completed: bool = Field(...)
    pinned: bool = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "title": "Buy a good present",
                "date": "27-02-2022",
                "completed": True,
                "pinned": False
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
