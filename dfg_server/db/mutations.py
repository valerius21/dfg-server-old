insert_photo = '''
mutation InsertPhoto(
  $acquaintance: Boolean = false, 
  $colleagues: Boolean = false,
  $family: Boolean = false, 
  $friends: Boolean = false, 
  $everybody: Boolean = false, 
  $nobody: Boolean = false, 
  $sensitivity: String!, 
  $is_private: Boolean!,
  $photo_id: Int!, 
  $uid: String!) {
  insert_results(objects: 
    {
      acquaintance: $acquaintance, 
      colleagues: $colleagues, 
      everybody: $everybody, 
      family: $family, 
      friends: $friends, 
      is_private: $is_private, 
      nobody: $nobody, 
      photo_id: $photo_id, 
      sensitivity: $sensitivity, 
      uid: $uid}) {
    affected_rows
  }
}
'''
