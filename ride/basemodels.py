from bson import ObjectId
from pydantic import BaseModel


class AssignRidePayload(BaseModel):
    user_id: str = ''
    start_location: str = ""
    end_location: str = ""

class CompleteRidePayload(BaseModel):
    ride_id: str = ''

class User(BaseModel):
    user_id: str = ''
