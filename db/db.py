from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
from graphql import DocumentNode

ENDPOINT = "https://c102-226.cloud.gwdg.de/v1/graphql"


class DB:
    transport = None
    client = None

    def __init__(self):
        self.transport = AIOHTTPTransport(url=ENDPOINT, headers={
            'content-type': 'application/json'
        })
        self.client = Client(transport=self.transport, fetch_schema_from_transport=True)

    def query(self, query: DocumentNode):
        result = self.client.execute(query)
        return result


if __name__ == '__main__':
    query = gql('''query PrivatePhotosCount {
          flickr_private_aggregate {
            aggregate {
              count
            }
          }
        }
    ''')

    db = DB()
    res = db.query(query)
    print(res)
