import numpy as np

from image.StudyImage import StudyImage


def add(a: int, b: int) -> int:
    return a + b


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


def get_all_image_structs(uid: str, sample_size=100) -> [StudyImage]:
    return [StudyImage(uid, v == 1, k + 1) for k, v in enumerate(private_distribution(sample_size))]
