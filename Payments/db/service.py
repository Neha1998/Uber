from Uber.Payments.db.models import Transaction

from Uber.Payments.utility import  Utility
class Service(object):

    transactions = []

    def list(self):
        return [self.embed(c) for c in self.transactions]

    def update(self, transaction_id):
        pass

    def create(self, ride_id):
        from Uber.ride.db.config import dbservice as ride_dbservice

        ride_obj = ride_dbservice.fetch(ride_id)
        cost = Utility().get_cost(ride_obj.km)
        discounted_cost = Utility().discounted_price(cost, ride_obj.coupon_id)

        payment = Transaction(coupon_id=ride_obj.coupon_id,
                              cost=cost, discounted_cost=discounted_cost)
        self.transactions.append(payment)
        return self.embed(payment)

    def delete(self, transaction_id):
        pass

    def embed(self,payment):
        return payment.__dict__
