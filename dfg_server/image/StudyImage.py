from dfg_server.config.config import Config


class StudyImage:
    """Study Image representation"""
    uid = None
    is_private = False
    i = 0
    index = None
    image_url: str = ""
    gwdg_url: str = ""
    image = None
    db_client = None

    def __init__(self, uid: str, is_private: bool, db_client):
        self.uid = uid
        self.is_private = is_private
        StudyImage.i += 1
        if StudyImage.i % 100 == 0:
            self.index = 100
        else:
            self.index = StudyImage.i % 100
        self.db_client = db_client

        if self.is_private:
            self.image = self.db_client.random_private_image()
            image_server = Config.image_server_private
        else:
            self.image = self.db_client.random_public_image()
            image_server = Config.image_server_public

        self.image_url = self.image['destination']
        self.filename = self.image_url.split("/")[-1]
        self.gwdg_url = f'{image_server}/{self.filename}'

    def __repr__(self):
        return f"UID: {self.uid}\tINDEX: {self.index}\tPRIVATE: {self.is_private}\tIMG:{self.image}"

    def to_dict(o):
        if isinstance(o, StudyImage):
            dict = {
                'uid': o.uid,
                'page_index': o.index,
                'is_private': o.is_private,
                'image_url': o.image_url,
                'image_id': o.image['id'],
                'filename': o.filename,
                'gwdg_url': o.gwdg_url
            }
            return dict
        else:
            type_name = o.__class__.__name__
            raise TypeError("Unexpected type {0}".format(type_name))
