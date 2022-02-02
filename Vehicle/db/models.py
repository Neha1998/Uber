import datetime
import uuid


class Vehicle:

    def __init__(self, driver_id, model, vehicle_no, curr_loc=0, _id=True):
        self.driver_id = driver_id
        self.model = model
        self.vehicle_no = vehicle_no
        self.current_loc = curr_loc
        self.active = 1 # 1-.available 2-busy in a ride, 0-deleted
        self.km = 0  # km driven during  a ride
        self.created_on = datetime.datetime.now()
        self.updated_on = datetime.datetime.now()
        self.id = uuid.uuid4() if _id else vehicle_no

    def save(self):
        pass
