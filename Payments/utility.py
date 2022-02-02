from Uber.CouponCode.db.config import dbservice as coupon_dbservice

class Utility(object):

    def __init__(self):
        self.default_cost = 5
        self.min_ride_price=50
        self.km_cost_map = {(1,3):10, (3,6):8}

    def get_cost(self, km_driven):
        import pdb;pdb.set_trace()
        cost = 0
        for i in range(1, km_driven):
            f=0
            for km, val in self.km_cost_map.items():
                if i in range(km[0], km[1]):
                    cost+=val
                    f=1
                    break
            if not f:
                cost+=(km_driven-i+1)*self.default_cost
                break
        cost = max(self.min_ride_price, cost)
        return cost

    @staticmethod
    def discounted_price(cost, coupon_id):
        coupon = coupon_dbservice.fetch(coupon_id=coupon_id)
        if coupon.value_discount:
            return cost-coupon.value_discount
        if coupon.percent_discount:
            return cost - (cost*coupon.percent_discount/100)