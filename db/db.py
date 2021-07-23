from gql import Client
from gql.transport.aiohttp import AIOHTTPTransport
from graphql import DocumentNode
from numpy.random import default_rng

from config.Config import Config
from queries import *

cfg = Config()
rng = default_rng()


# TODO: verify if image is available (Status 200)

class DB:
    transport = None
    client = None

    def __init__(self):
        self.transport = AIOHTTPTransport(url=cfg.endpoint)
        self.client = Client(transport=self.transport, fetch_schema_from_transport=True)

    def query(self, graphql_query: DocumentNode) -> dict:
        """query a gql set"""
        result = self.client.execute(graphql_query)
        return result

    def mutate(self):
        """mutate gql"""
        pass

    def subscribe(self):
        pass

    def private_count(self) -> int:
        """count all the private photos"""
        return self.client.execute(count_private())['flickr_private_aggregate']['aggregate']['count']

    def public_count(self) -> int:
        """count all the public photos"""
        return self.client.execute(count_public())['flickr_public_aggregate']['aggregate']['count']

    def random_public_image(self) -> dict:
        """count all the private photos"""
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
        doc = self.client.execute(public_image_by_index(), variable_values={"_eq": img_id})
        doc = doc['flickr_public'][0]
        return doc

    def private_image_by_id(self, img_id: int) -> dict:
        """get image by id"""
        doc = self.client.execute(private_image_by_index(), variable_values={"_eq": img_id})
        doc = doc['flickr_private'][0]
        return doc
    # TODO: post requests from frontend


if __name__ == '__main__':
    db = DB()
    print('public image by id', db.public_image_by_id(15))
    print('public image by id', db.private_image_by_id(15))
    print('private count', db.private_count())
    print('public count', db.public_count())
    print('random private', db.random_private_image())
    print('random public', db.random_public_image())
