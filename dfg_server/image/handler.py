import numpy as np

from dfg_server.config.config import Config
from dfg_server.db.db import DB
from dfg_server.db.submission import Submission
from dfg_server.image.StudyImage import StudyImage


def _private_distribution(sample_size=100) -> [bool]:
    """create a distribution for the study size regarding the privacy aspect"""
    if sample_size % 2 == 0:
        n = int(sample_size / 2)
        m = n
    else:
        n = int(sample_size / 2)
        m = n + 1
    dist = np.ones(sample_size)
    dist[:m] = 0
    np.random.shuffle(dist)
    return [bool(n == 1) for n in dist]


def get_all_image_structs(uid: str, sample_size=100):
    """generates all images"""
    images = list()
    is_accumulating = Config.accumulate_results
    private_ids = DB.get_private_submissions()
    public_ids = DB.get_public_submissions()
    for is_private in _private_distribution(sample_size):
        img = None
        if is_private and is_accumulating:
            if private_ids:
                img = DB.private_image_by_id(private_ids.pop())
            else:
                img = DB.random_private_image()
        else:
            if public_ids and is_accumulating:
                img = DB.public_image_by_id(public_ids.pop())
            else:
                img = DB.random_public_image()
        images.append(StudyImage(uid, is_private, img).to_dict())
    return images


def add_submission(submission: Submission) -> dict:
    """validate and insert the form submission"""
    # TODO: validate entries
    # TODO: query image ID and increment submission count
    return DB.insert_submission(submission)
