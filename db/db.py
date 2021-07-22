from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
from graphql import DocumentNode

from config.Config import Config


class DB:
    transport = None
    client = None

    def __init__(self):
        cfg = Config()
        self.transport = AIOHTTPTransport(url=cfg.endpoint, headers={
            'content-type': 'application/json'
        })
        self.client = Client(transport=self.transport, fetch_schema_from_transport=True)

    def query(self, graphql_query: DocumentNode) -> dict:
        result = self.client.execute(graphql_query)
        return result


if __name__ == '__main__':
    count_private_query = gql('''query PrivatePhotosCount {
          flickr_private_aggregate {
            aggregate {
              count
            }
          }
        }
    ''')

    db = DB()
    res = db.query(count_private_query)
    print(res)
