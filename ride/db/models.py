import datetime
import uuid


class Ride:

    def __init__(self, user_id, vehicle_id, driver_id):
        self.user_id = user_id
        self.vehicle_id = vehicle_id
        self.driver_id = driver_id
        self.active = 1
        self.created_on = datetime.datetime.now()
        self.updated_on = datetime.datetime.now()
        self.cost = None
        self.km = 0
        self.id = uuid.uuid4()

    def save(self):
        pass
