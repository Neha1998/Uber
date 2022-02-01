from Uber.Vehicle.db.config import dbservice
class Manager():
    def __init__(self,user_id=None):
        self.user_id =  user_id

    def get(self):
        return dbservice.get()

    def create(self, name, model, veh_no):
        res = dbservice.create(name, model, veh_no)
        return res
