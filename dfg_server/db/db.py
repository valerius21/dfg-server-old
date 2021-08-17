from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport
from numpy.random import default_rng

from dfg_server.config.config import Config
from dfg_server.db.mutations import insert_photo
from dfg_server.db.queries import *
from dfg_server.db.submission import Submission

cfg = Config()
rng = default_rng()


class DB:
    """DB interaction instance"""
    transport = None
    client = None
    count = {
        'public': -1,
        'private': -1
    }

    def __init__(self):
        DB.transport = RequestsHTTPTransport(url=cfg.endpoint)
        DB.client = Client(transport=DB.transport, fetch_schema_from_transport=True)

    @staticmethod
    def _get_count(visibility: str) -> int:
        """get photo count from a certain visibility"""
        if visibility == 'private':
            queue = gql(count_private)
        else:
            queue = gql(count_public)
        result = DB.client.execute(queue)
        count: int = int(result[f'flickr_{visibility}_aggregate']['aggregate']['count'])
        DB.count[visibility] = count
        return count

    @staticmethod
    def private_count() -> int:
        """count all the private photos"""
        if DB.count['private'] == -1:
            return DB._get_count('private')
        return DB.count['private']

    @staticmethod
    def public_count() -> int:
        """count all the public photos"""
        if DB.count['public'] == -1:
            return DB._get_count('public')
        return DB.count['public']

    @staticmethod
    def random_public_image() -> dict:
        """count all the private photos"""
        # TODO: fix non-existent IDs
        high = DB.public_count()
        random_id = rng.integers(low=1, high=high, size=1)[0]
        return DB.public_image_by_id(int(random_id))

    @staticmethod
    def random_private_image() -> dict:
        """count all the private photos"""
        high = DB.private_count()
        random_id = rng.integers(low=1, high=high, size=1)[0]
        return DB.private_image_by_id(int(random_id))

    @staticmethod
    def public_image_by_id(img_id: int) -> dict:
        """get image by id"""
        doc = DB.client.execute(gql(public_image_by_index), variable_values={"_eq": img_id})
        doc = doc['flickr_public'][0]
        return doc

    @staticmethod
    def private_image_by_id(img_id: int) -> dict:
        """get image by id"""
        doc = DB.client.execute(gql(private_image_by_index), variable_values={"_eq": img_id})
        doc = doc['flickr_private'][0]
        return doc

    @staticmethod
    def _rand_int(high: int, low=1) -> int:
        """rng"""
        return rng.integers(low, high=high, size=1)[0]

    @staticmethod
    def insert_submission(submission: Submission) -> dict:
        """insert form submission into db"""
        mutation = gql(insert_photo)
        values = {
            "acquaintance": submission.acquaintance,
            "colleagues": submission.colleagues,
            "family": submission.family,
            "friends": submission.friends,
            "everybody": submission.everybody,
            "nobody": submission.nobody,
            "sensitivity": submission.sensitivity,
            "is_private": submission.is_private,
            "photo_id": submission.photo_id,
            "uid": submission.uid
        }
        return DB.client.execute(mutation, variable_values=values)
