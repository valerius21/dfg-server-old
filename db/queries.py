from gql import gql


def count_private():
    """count all private images in DB"""
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
    """count all public images in DB"""
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
    """get a public image by ID"""
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
    """get a private image by ID"""
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


def private_priority_image_by_index():
    """get a private image by ID with 1 <= n <= 40 submissions"""
    query = '''
            query PrivatePriority($_eq: bigint, $_lte: Int = 40) {
              flickr_private(where: {submissions: {_gte: 1, _lte: $_lte}, id: {_eq: $_eq}}) {
                destination
                id
                source
                submissions
              }
            }
        '''
    return gql(query)


def public_priority_image_by_index():
    """get a public image by ID with 1 <= n <= 40 submissions"""
    query = '''
            query PublicPriority($_eq: bigint, $_lte: Int = 40) {
              flickr_public(where: {submissions: {_gte: 1, _lte: $_lte}, id: {_eq: $_eq}}) {
                destination
                id
                source
                submissions
              }
            }
        '''
    return gql(query)
