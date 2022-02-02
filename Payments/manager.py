from Uber.Payments.db.config import dbservice

class Manager(object):
    def __init__(self,t_id=None):
        self.t_id =  t_id

    def list(self):
        return dbservice.list()

    def create(self, ride_id):
        res = dbservice.create(ride_id)
        return res

    def delete(self):
        pass

    def update(self):
        pass
