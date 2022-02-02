from Uber.CouponCode.db.config import dbservice

class Manager(object):
    def __init__(self,coupon_id=None):
        self.coupon_id =  coupon_id

    def list(self):
        return dbservice.list()

    def create(self, code, value_discount, percent_discount):
        res = dbservice.create(code, value_discount, percent_discount)
        return res

    def delete(self):
        dbservice.delete(self.coupon_id)

    def update(self):
        pass

    def list_all_coupon_ids(self):
        return [str(c['id']) for c in self.list()]

