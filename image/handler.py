import numpy as np

from db.db import DB
from image.StudyImage import StudyImage

db = DB()


def private_distribution(sample_size=100) -> [int]:
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
    # TODO: make comprehension async
    imgs = [StudyImage(uid, bool(v == 1), db) for v in private_distribution(sample_size)]
    return [i.to_dict() for i in imgs]
