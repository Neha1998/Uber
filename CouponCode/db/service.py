from Uber.CouponCode.db.models import Coupon

class Service(object):

    coupons = [Coupon('VALUE_50', 50 ,None, False),
                     Coupon('VALUE_10', 10 , None, False),
                     Coupon('PERCENT_10', None, 10, False),
                     Coupon('PERCENT_5', None, 5, False)]

    def list(self):
        return [self.embed(c) for c in self.coupons]

    def update(self, coupon_id):
        pass

    def fetch(self, coupon_code=None, coupon_id=None):
        for c in self.coupons:
            if str(c.id)==coupon_id or str(c.coupon_code)==coupon_code:
                return c

    def create(self, code, value_discount=None, percent_discount=None):

        if not value_discount and not percent_discount:
            return dict(status=False, message="Failed to create coupon - missing discount")

        coupon = Coupon(code, int(value_discount), int(percent_discount))
        self.coupons.append(coupon)
        return self.embed(coupon)

    def delete(self, coupon_id):
        for c in self.coupons:
            if str(c.id) == coupon_id:
                c.active = -1
                c.save()
                return

    def embed(self,coupon):
        return coupon.__dict__
