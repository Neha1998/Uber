from Uber.Vehicle.db.config import dbservice
class Manager():
    def __init__(self,user_id=None):
        self.user_id =  user_id

    def get(self):
        return dbservice.get()

    def create(self, driver_id, model, veh_no, curr_loc):
        res = dbservice.create(driver_id, model, veh_no, curr_loc)
        return res

    def udpate_vehicle(self, veh_id, veh_loc, km_driven=None):
        res = dbservice.update(veh_id, loc=veh_loc, km=km_driven)
        return res
