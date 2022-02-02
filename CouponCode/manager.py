from Uber.CouponCode.db.config import dbservice

class Manager(object):
    def __init__(self,coupon_id=None):
        self.coupon_id =  coupon_id

    def list(self):
        return dbservice.list()

    def create(self, name, email, mobile):
        res = dbservice.create(user_name=name, email=email, mobile=mobile)
        return res

    def delete(self):
        dbservice.delete(self.coupon_id)

    def update(self):
        pass
