from fastapi import FastAPI

from config.config import Config
from image.handler import get_all_image_structs

app = FastAPI()


@app.get("/images/all/{uid}")
def get_image_set_for_uid(uid: str):
    """Get all initial images with a size of 100, preferably 40 submissions per image 50% private images."""
    # TODO: make async
    images = get_all_image_structs(uid, Config.study_size)
    res = {'images': images}
    return res

# uvicorn main:app --reload
