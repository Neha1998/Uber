from Uber.Vehicle.db.models import Vehicle

class Service(object):

    vehicles = [Vehicle('driver-1', 'a', 'v-1',4, False),
                      Vehicle('driver-2', 'b','v-2',6, False)]

    def get(self):
        return [self.embed(v) for v in self.vehicles]

    def create(self, name, model, veh_no, curr_loc):
        veh = Vehicle(name, model, veh_no, curr_loc)
        self.vehicles.append(veh)
        return self.embed(veh)

    def delete(self):
        pass

    def embed(self,veh):
        return veh.__dict__

    def update(self, veh_id, loc=None, active=None, km=None):
        for veh in self.vehicles:
            if str(veh.id) == veh_id:
                veh.current_loc = int(loc) if loc is not None else veh.current_loc
                veh.active = int(active) if active is not None else veh.active
                veh.km = int(km) if km is not None else veh.km
                veh.save()
                return veh

    def get_vehicle(self, active, radius, curr_loc):
        for veh in self.vehicles:
            if veh.active==active and int(veh.current_loc) in range(curr_loc+radius):
                return veh