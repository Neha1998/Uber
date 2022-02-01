import datetime
import uuid


class Vehicle:

    def __init__(self, name, model, vehicle_no):
        self.name = name
        self.model = model
        self.vehicle_no = vehicle_no
        self.active = 1
        self.created_on = datetime.datetime.now()
        self.updated_on = datetime.datetime.now()
        self.id = uuid.uuid4()

    def save(self):
        pass
