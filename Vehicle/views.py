from fastapi import APIRouter, Request, Response, status

from Uber.Vehicle.basemodels import Payload, LocationPayload
from Uber.Vehicle.manager import Manager

vehicle_router = APIRouter()


@vehicle_router.get('/api/vehicles')
async def list_all_vehicles(request: Request):
    """
    This API lists all vehicles
    """
    res = Manager().get()
    return res

@vehicle_router.post('/api/vehicles')
async def create_vehicle(request: Request, payload: Payload):
    """
    This API creates a vehicle
    """
    res = Manager().create(payload.driver_id, payload.model, payload.vehicle_no, payload.current_location)
    return res


@vehicle_router.patch('/api/vehicles/{veh_id}')
async def update_vehicle(request: Request, veh_id, payload: LocationPayload):
    """
    This API updates the vehicle location and km driven during a ride.
    """
    res = Manager().udpate_vehicle(veh_id, payload.location, km_driven=payload.km)
    return res
