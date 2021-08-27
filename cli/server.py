import os

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from fastapi.responses import RedirectResponse

from dfg_server.config.config import Config
from dfg_server.db.submission import Submission
from dfg_server.routes.image import get_image_set_for_uid_accumulated, get_image_set_for_uid
from dfg_server.routes.submit import submit_image_evaluation_request

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


@app.get("/api/images/acc/{uid}")
def image_set_for_uid_accumulated(uid: str):
    """Get all initial images with a size of 100, preferably 40 submissions per image 50% private images."""
    return get_image_set_for_uid_accumulated(uid)


@app.get("/api/images/not-acc/{uid}")
def image_set_for_uid_not_accumulated(uid: str):
    """Get all initial images with a size of 100, with 50% private images."""
    return get_image_set_for_uid(uid)


@app.post("/api/submit")
def submit_image_evaluation(submission: Submission):
    """handle incoming form submissions. returns the affected rows."""
    return submit_image_evaluation_request(submission)


@app.get("/")
def index():
    """redirect to /docs. /redoc is also an option"""
    return RedirectResponse("/docs")


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="DFG API",
        version="0.0.2",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": f"{Config.image_server_public.split('/public')[0]}/assets/logo.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

if __name__ == '__main__':
    is_prod = os.environ['DFG_PRODUCTION']
    uvicorn.run("server:app", host='0.0.0.0', reload=not is_prod, port=Config.port)
