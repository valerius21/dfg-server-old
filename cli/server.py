import os
import sys

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from dfg_server.config.config import Config
from dfg_server.db.submission import Submission
from dfg_server.image.handler import get_all_image_structs, add_submission

app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=[
                       'http://localhost:3000',
                       'https://localhost:3000',
                       'https://localhost:443',
                       'https://localhost',
                       'http://localhost:80',
                       'http://localhost',
                       '*'
                   ],
                   allow_methods=['*'],
                   allow_headers=['*'],
                   allow_credentials=True
                   )


@app.get("/api/images/{uid}")
def get_image_set_for_uid(uid: str):
    """Get all initial images with a size of 100, preferably 40 submissions per image 50% private images."""
    images = get_all_image_structs(uid, Config.study_size)
    res = {'images': images}
    return res


@app.post("/api/submit")
def submit_image_evaluation(submission: Submission):
    """handle incoming form submissions. returns the affected rows."""
    return add_submission(submission)


@app.get("/")
def index():
    """redirect to /docs. /redoc is also an option"""
    return RedirectResponse("/docs")


if __name__ == '__main__':
    is_prod = os.environ['DFG_PRODUCTION']
    uvicorn.run("server:app", reload=not is_prod, port=Config.port)
