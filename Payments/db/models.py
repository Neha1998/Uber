import datetime
import uuid


class Transaction:

    def __init__(self, coupon_id=None, cost=0, discounted_cost=0):
        self.coupon_id = coupon_id
        self.cost = cost
        self.discounted_cost = discounted_cost
        self.active = 1
        self.created_on = datetime.datetime.now()
        self.updated_on = datetime.datetime.now()
        self.id = uuid.uuid4()

    def save(self):
        pass
