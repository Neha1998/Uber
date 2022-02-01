import datetime
import uuid


class User:

    def __init__(self, name, email, mobile, _id=True):
        self.name = name
        self.email = email
        self.mobile = mobile
        self.active = 1
        self.created_on = datetime.datetime.now()
        self.updated_on = datetime.datetime.now()
        self.id = uuid.uuid4() if _id else name

    def save(self):
        pass
