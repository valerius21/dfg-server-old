from dfg_server.config.config import Config
from dfg_server.image.handler import get_all_image_structs


def get_image_set_for_uid_accumulated(uid: str):
    """Get all initial images with a size of 100, preferably 40 submissions per image 50% private images."""
    images = get_all_image_structs(uid, Config.study_size, is_accumulating=True)
    res = {'images': images}
    return res


def get_image_set_for_uid(uid: str):
    """Get all initial images with a size of 100, 50% private images."""
    images = get_all_image_structs(uid, Config.study_size, is_accumulating=False)
    res = {'images': images}
    return res
