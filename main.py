from typing import Optional

from fastapi import FastAPI

from image.handler import get_all_image_structs

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/images/all/{uid}")
def get_set(uid: str):
    imgs = get_all_image_structs(uid)
    res = {'images': imgs}
    return res

# uvicorn main:app --reload
