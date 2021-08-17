from collections import Counter

from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport
from graphql import DocumentNode
from numpy.random import default_rng

from dfg_server.config.config import Config
from dfg_server.db.mutations import insert_photo
from dfg_server.db.queries import *
from dfg_server.db.submission import Submission

cfg = Config()
rng = default_rng()


class DB:
    """DB interaction instance"""
    transport = RequestsHTTPTransport(url=cfg.graphql_endpoint)
    client = Client(transport=transport, fetch_schema_from_transport=True)
    count = {
        'public': -1,
        'private': -1
    }

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

    @staticmethod
    def _filter_for_submission_ids(query: DocumentNode) -> [int]:
        """filters for all submissions under the accumulation size @Config.accumulation_size"""
        acc = Config.accumulation_size + 1
        response = DB.client.execute(query)
        # Count occurrences of every ID
        elements = Counter([submission['photo_id'] for submission in response['results']])
        # Filter for acc size
        elements = filter(lambda x: x[1] < acc,
                          [(submissions_by_count, elements[submissions_by_count]) for submissions_by_count in elements])
        # return ID of filtered elements
        return [submission[0] for submission in elements]

    @staticmethod
    def get_public_submissions() -> [int]:
        """:returns IDs of preferred pictures due to accumulation size regarding the public set"""
        return DB._filter_for_submission_ids(gql(public_submissions_photo_ids))

    @staticmethod
    def get_private_submissions() -> [int]:
        """:returns IDs of preferred pictures due to accumulation size regarding the private set"""
        return DB._filter_for_submission_ids(gql(private_submissions_photo_ids))


if __name__ == '__main__':
    print(DB.get_private_submissions())
