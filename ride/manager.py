from Uber.ride.db.config import dbservice
from Uber.Vehicle.db.config import  dbservice as vehicle_db_service
class Manager(object):
    def __init__(self,user_id=None):
        self.user_id =  user_id

    def get_user_rides(self, user_id):
        return dbservice.get_user_rides(user_id)

    def get_driver_rides(self, user_id):
        return dbservice.get_driver_rides(user_id)

    def assign_ride(self, user_id, start_loc, end_loc, radius=2):

        # on the basis of start_loc fetch vehicle with active=1 and current_location within radius distance from start_loc
        vehicle = vehicle_db_service.get_vehicle(active=1, radius=radius, curr_loc = int(start_loc))

        #lock the vehicle
        vehicle_db_service.update(str(vehicle.id), active=2)

        #initiate a ride
        ride = dbservice.create(user_id, vehicle.id, vehicle.driver_id)

        return dbservice.embed(ride)

    def complete_ride(self, ride_id, km_driven):
        # set status of ride to 2  and update cost and km
        ride = dbservice.complete_ride(ride_id, km_driven)

        # free the vehicle
        vehicle_db_service.update(ride.vehicle_id, active=1, km=0)

        return dbservice.embed(ride)

