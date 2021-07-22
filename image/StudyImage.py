class StudyImage:
    uid = None
    is_private = False
    index = None
    imageURL = ""

    def __init__(self, uid, is_private, index):
        self.uid = uid
        self.is_private = is_private
        self.index = index

    def __repr__(self):
        return f"UID: {self.uid}\tINDEX: {self.index}\tPRIVATE: {self.is_private}"
