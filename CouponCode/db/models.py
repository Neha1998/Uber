import datetime
import uuid


class Coupon:

    def __init__(self, code, value_discount=0, percent_discount=0, _id=True):
        self.code = code
        self.value_discount= value_discount
        self.percent_discount = percent_discount
        self.active = 1
        self.created_on = datetime.datetime.now()
        self.updated_on = datetime.datetime.now()
        self.id = uuid.uuid4() if _id else code

    def save(self):
        pass
