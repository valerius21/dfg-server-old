class StudyImage:
    uid = None
    is_private = False
    i = 0
    index = None
    image_url = ""
    image = None
    db_client = None

    def __init__(self, uid: str, is_private: bool, db_client):
        self.uid = uid
        self.is_private = is_private
        StudyImage.i += 1
        self.index = StudyImage.i
        self.db_client = db_client

        if self.is_private:
            self.image = self.db_client.random_private_image()
            # self.image_url = f"{Config.image_server_private}/{self.image['filename']}"
        else:
            self.image = self.db_client.random_public_image()
            # self.image_url = f"{Config.image_server_public}/{self.image['filename']}"

        self.image_url = self.image

    def __repr__(self):
        return f"UID: {self.uid}\tINDEX: {self.index}\tPRIVATE: {self.is_private}\tIMG:{self.image}"

    def to_dict(o):
        if isinstance(o, StudyImage):
            dict = {
                'uid': o.uid,
                'page_index': o.index,
                'is_private': o.is_private,
                'image_url': o.image_url,
                'image_id': o.image['id']
            }
            return dict
        else:
            type_name = o.__class__.__name__
            raise TypeError("Unexpected type {0}".format(type_name))
