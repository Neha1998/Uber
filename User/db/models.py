import datetime
import uuid


class User:

    def __init__(self, name, email, mobile):
        self.name = name
        self.email = email
        self.mobile = mobile
        self.active = 1
        self.created_on = datetime.datetime.now()
        self.updated_on = datetime.datetime.now()
        self.id = uuid.uuid4()

    def save(self):
        pass
