from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport
from numpy.random import default_rng

from dfg_server.config.config import Config
from dfg_server.db.mutations import insert_photo
from dfg_server.db.queries import *
from dfg_server.db.submission import Submission

cfg = Config()
rng = default_rng()


# TODO: verify if image is available (Status 200)

class DB:
    transport = None
    client = None

    def __init__(self):
        DB.transport = RequestsHTTPTransport(url=cfg.endpoint)
        self.client = Client(transport=DB.transport, fetch_schema_from_transport=True)

    def private_count(self) -> int:
        """count all the private photos"""
        result = self.client.execute(gql(count_private))
        return result['flickr_private_aggregate']['aggregate']['count']

    def public_count(self) -> int:
        """count all the public photos"""
        result = self.client.execute(gql(count_public))
        return result['flickr_public_aggregate']['aggregate']['count']

    def random_public_image(self) -> dict:
        """count all the private photos"""
        # TODO: fix non-existent IDs
        high = self.public_count()
        random_id = rng.integers(low=1, high=high, size=1)[0]
        return self.public_image_by_id(int(random_id))

    def random_private_image(self) -> dict:
        """count all the private photos"""
        high = self.private_count()
        random_id = rng.integers(low=1, high=high, size=1)[0]
        return self.private_image_by_id(int(random_id))

    def public_image_by_id(self, img_id: int) -> dict:
        """get image by id"""
        doc = self.client.execute(gql(public_image_by_index), variable_values={"_eq": img_id})
        doc = doc['flickr_public'][0]
        return doc

    def private_image_by_id(self, img_id: int) -> dict:
        """get image by id"""
        doc = self.client.execute(gql(private_image_by_index), variable_values={"_eq": img_id})
        doc = doc['flickr_private'][0]
        return doc

    @staticmethod
    def _rand_int(high: int, low=1) -> int:
        """rng"""
        return rng.integers(low, high=high, size=1)[0]

    # TODO: post requests from frontend

    def insert_submission(self, submission: Submission) -> dict:
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
        return self.client.execute(mutation, variable_values=values)


if __name__ == '__main__':
    db = DB()
    print('public image by id', db.public_image_by_id(15))
    print('private image by id', db.private_image_by_id(66))
    print('private count', db.private_count())
    print('public count', db.public_count())
    print('random private', db.random_private_image())
    print('random public', db.random_public_image())
