import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from dfg_server.config.config import Config
from dfg_server.db.submission import Submission
from dfg_server.image.handler import get_all_image_structs, add_submission

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=['*'])


@app.get("/images/all/{uid}")
def get_image_set_for_uid(uid: str):
    """Get all initial images with a size of 100, preferably 40 submissions per image 50% private images."""
    images = get_all_image_structs(uid, Config.study_size)
    res = {'images': images}
    return res


@app.post("/submit")
def submit_image_evaluation(submission: Submission):
    """handle incoming form submissions. returns the affected rows."""
    return add_submission(submission)


if __name__ == '__main__':
    uvicorn.run("server:app", reload=True)
