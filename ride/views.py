from fastapi import APIRouter, Request

from Uber.ride.basemodels import AssignRidePayload, User
from Uber.ride.manager import Manager

ride_router = APIRouter()


@ride_router.post('/api/rides')
async def assign_ride(request: Request, payload: AssignRidePayload ):
    """
    This API creates a vehicle
    """
    res = Manager().assign_ride(payload.user_id, payload.start_location, payload.end_location)
    return res


@ride_router.get('/api/user_rides/{user_id}')
async def list_all_user_rides(request: Request, user_id):
    """
    This API lists all user rides
    """
    res = Manager().get_user_rides(user_id)
    return res

@ride_router.get('/api/driver_rides/{user_id}')
async def list_all_driver_rides(request: Request, user_id):
    """
    This API lists all driver rides
    """
    res = Manager().get_driver_rides(user_id)
    return res

@ride_router.post('/api/complete_ride/{ride_id}')
async def complete_ride(request: Request, ride_id, km_driven):
    """
    This API creates a vehicle
    """
    res = Manager().complete_ride(ride_id, km_driven)
    return res