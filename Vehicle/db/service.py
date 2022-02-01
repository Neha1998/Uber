from Uber.Vehicle.db.models import Vehicle

class Service(object):

    vehicles = []

    def get(self):
        return [self.embed(v) for v in self.vehicles]

    def update(self, vehicle_id):
        pass

    def create(self, name, model, veh_no):
        veh = Vehicle(name, model, veh_no)
        self.vehicles.append(veh)
        return self.embed(veh)

    def delete(self):
        pass

    def embed(self,user):
        return user.__dict__
