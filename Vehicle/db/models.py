import datetime
import uuid


class Vehicle:

    def __init__(self, driver_id, model, vehicle_no, _id=True):
        self.driver_id = driver_id
        self.model = model
        self.vehicle_no = vehicle_no
        self.current_loc = None
        self.active = 1
        self.km = 0
        self.created_on = datetime.datetime.now()
        self.updated_on = datetime.datetime.now()
        self.id = uuid.uuid4() if _id else vehicle_no

    def save(self):
        pass
