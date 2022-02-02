from Uber.ride.db.models import Ride
from Uber.Payments.manager import Manager as payment_manager
class Service(object):

    rides = []

    def get(self):
        return [self.embed(v) for v in self.rides]

    def update(self, ride_id):
        pass

    def fetch(self, ride_id):
        for ride in self.rides:
            if str(ride.id) == ride_id:
                return ride

    def create(self, user_id, vehicle_id, driver_id, coupon_id):
        ride = Ride(user_id, vehicle_id, driver_id, coupon_id)
        self.rides.append(ride)
        return ride

    def delete(self):
        pass

    def embed(self,ride):
        return ride.__dict__

    def get_user_rides(self, user_id):
        res = [ ride for ride in self.rides if ride.user_id == user_id]
        return res

    def get_driver_rides(self, driver_id):
        res = [ride for ride in self.rides if ride.driver_id == driver_id]
        return res

    def complete_ride(self, ride_id, km_driven):
        ride = self.fetch(ride_id)

        if ride.active == 2:
            return dict(status=False, message="Already completed ride.")

        ride.active = 2  #completed
        ride.km = km_driven
        ride.cost = payment_manager().create(ride_id)
        ride.save()
        return ride