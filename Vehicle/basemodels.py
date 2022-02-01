from bson import ObjectId
from pydantic import BaseModel


class Payload(BaseModel):
    name: str = ""
    model: str = ""
    vehicle_no: str = ""