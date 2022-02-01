from fastapi import APIRouter, Request, Response, status

from Uber.Vehicle.basemodels import Payload
from Uber.Vehicle.manager import Manager

vehicle_router = APIRouter()


@vehicle_router.get('/api/vehicles')
async def list_all_vehicles(request: Request, api_response: Response):
    """
    This API lists all vehicles
    """
    res = Manager().get()
    return res

@vehicle_router.post('/api/vehicles')
async def create_vehicle(request: Request, payload: Payload,api_response: Response):
    """
    This API creates a vehicle
    """
    res = Manager().create(payload.name, payload.model, payload.vehicle_no)
    return res