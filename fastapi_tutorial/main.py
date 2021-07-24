from typing import Optional

from pydantic import BaseModel
from fastapi import FastAPI, Query, Path, Body


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


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
    body: Item = Body(..., embed=True)
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
