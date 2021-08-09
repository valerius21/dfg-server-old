import numpy as np

from dfg_server.db.db import DB
from dfg_server.db.submission import Submission
from dfg_server.image.StudyImage import StudyImage

db = DB()


def _private_distribution(sample_size=100) -> [int]:
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
    return dist


def get_all_image_structs(uid: str, sample_size=100) -> [str]:
    """generates all images"""
    images = [StudyImage(uid, bool(v == 1), db) for v in _private_distribution(sample_size)]
    return [i.to_dict() for i in images]


def add_submission(submission: Submission) -> dict:
    """validate and insert the form submission"""
    # TODO: validate entries
    return db.insert_submission(submission)
