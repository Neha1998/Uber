from fastapi import APIRouter, Request, Response, status

from Uber.User.basemodels import UserPayload
from Uber.User.manager import UserManager

user_router = APIRouter()


@user_router.get('/api/users')
async def list_all_users(request: Request, api_response: Response):
    """
    This API lists all users
    """
    res = UserManager().get_users()
    return res

@user_router.post('/api/users')
async def create_user(request: Request, payload: UserPayload,api_response: Response):
    """
    This API creates a user
    """
    res = UserManager().create_user(payload.name, payload.email, payload.mobile)
    return res