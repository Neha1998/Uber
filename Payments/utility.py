from Uber.CouponCode.db.config import dbservice as coupon_dbservice

class Utility(object):
    @staticmethod
    def get_cost(km_driven):
        return km_driven*100

    @staticmethod
    def discounted_price(cost, coupon_id):
        coupon = coupon_dbservice.fetch(coupon_id=coupon_id)
        if coupon.value_discount:
            return cost-coupon.value_discount
        if coupon.percent_discount:
            return cost - (cost*coupon.percent_discount/100)