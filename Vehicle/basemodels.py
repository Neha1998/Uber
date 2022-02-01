from bson import ObjectId
from pydantic import BaseModel


class Payload(BaseModel):
    driver_id: str = ""
    model: str = ""
    vehicle_no: str = ""


class LocationPayload(BaseModel):
    location: str = ""
    km: int = 0