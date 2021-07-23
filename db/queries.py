from gql import gql


def count_private():
    query = '''query PrivatePhotosCount {
          flickr_private_aggregate {
            aggregate {
              count
            }
          }
        }
    '''
    return gql(query)


def count_public():
    query = '''
    query PublicPhotosCount {
          flickr_public_aggregate {
            aggregate {
              count
            }
          }
        }
    '''
    return gql(query)


def public_image_by_index():
    query = '''
        query PublicPhotosCount($_eq: bigint) {
          flickr_public(where: {id: {_eq: $_eq}}) {
            destination
            id
            source
          }
        }
    '''

    return gql(query)


def private_image_by_index():
    query = '''
        query PrivatePhotosCount($_eq: bigint) {
          flickr_private(where: {id: {_eq: $_eq}}) {
            destination
            id
            source
          }
        }
    '''

    return gql(query)
