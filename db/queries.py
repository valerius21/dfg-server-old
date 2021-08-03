from gql import gql


def count_private():
    """count all private images in DB"""
    query = '''query _PrivatePhotosCount {
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
    query _PublicPhotosCount {
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
        query _PublicPhotosCount($_eq: bigint) {
          flickr_public(where: {id: {_eq: $_eq}}) {
            filename
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
        query _PrivatePhotosCount($_eq: bigint) {
          flickr_private(where: {id: {_eq: $_eq}}) {
            filename
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
            query _PrivatePriority($_eq: bigint, $_lte: Int = 40) {
              flickr_private(where: {submissions: {_gte: 1, _lte: $_lte}, id: {_eq: $_eq}}) {
                filename
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
            query _PublicPriority($_eq: bigint, $_lte: Int = 40) {
              flickr_public(where: {submissions: {_gte: 1, _lte: $_lte}, id: {_eq: $_eq}}) {
                filename
                destination
                id
                source
                submissions
              }
            }
        '''
    return gql(query)
