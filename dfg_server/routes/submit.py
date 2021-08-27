from dfg_server.db.submission import Submission
from dfg_server.image.handler import add_submission


def submit_image_evaluation_request(submission: Submission):
    """handle incoming form submissions. returns the affected rows."""
    return add_submission(submission)
