count_private = '''query _PrivatePhotosCount {
          flickr_private_aggregate {
            aggregate {
              count
            }
          }
        }
    '''

count_public = '''
    query _PublicPhotosCount {
          flickr_public_aggregate {
            aggregate {
              count
            }
          }
        }
    '''

public_image_by_index = '''
        query _PublicPhotosCount($_eq: bigint!) {
          flickr_public(where: {id: {_eq: $_eq}}) {
            destination
            id
            source
          }
        }
    '''

private_image_by_index = '''
        query _PrivatePhotosCount($_eq: bigint!) {
          flickr_private(where: {id: {_eq: $_eq}}) {
            destination
            id
            source
          }
        }
    '''

private_priority_image_by_index = '''
            query _PrivatePriority($_eq: bigint!, $_lte: Int = 40) {
              flickr_private(where: {submissions: {_gte: 1, _lte: $_lte}, id: {_eq: $_eq}}) {
                destination
                id
                source
                submissions
              }
            }
        '''

public_priority_image_by_index = '''
            query _PublicPriority($_eq: bigint!, $_lte: Int = 40) {
              flickr_public(where: {submissions: {_gte: 1, _lte: $_lte}, id: {_eq: $_eq}}) {
                destination
                id
                source
                submissions
              }
            }
        '''
