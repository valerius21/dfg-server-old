from fastapi import FastAPI

from image.handler import get_all_image_structs

app = FastAPI()


@app.get("/images/all/{uid}")
def get_set(uid: str):
    """Get all initial images with a size of 100, preferably 40 submissions per image 50% private images."""
    # TODO: make async
    images = get_all_image_structs(uid)
    res = {'images': images}
    return res

# uvicorn main:app --reload
