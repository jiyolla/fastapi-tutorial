from datetime import datetime
from typing import List, Set, Optional

from pydantic import BaseModel, Field, HttpUrl
from fastapi import FastAPI, Query, Path, Body, Cookie


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float = Field(gt=0, example=110)
    tax: Optional[float] = None
    tags: Set[str] = set()
    image: Optional[List[Image]] = None
    expire_by: Optional[datetime] = None
    
    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "name": "Foo",
    #             "description": "A very nice Item",
    #             "price": 35.4,
    #             "tax": 3.2,
    #         }
    #     }


app = FastAPI()


@app.get("/items/{items_id}")
async def read_items(
    items_id: int = Path(..., title="Some title", description="Should be positive", gt=0),
    q: Optional[str] = Query(
        None,
        alias="item-query",
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        regex="^fixedquery$",
        deprecated=True,
    ),
    body: Item = Body(..., 
        examples={
            "normal": {
                "summary": "A summary",
                "description": "A normal example",
                "value": {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            }
        }   
    ),
    ads_id: Optional[str] = Cookie(None)
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
