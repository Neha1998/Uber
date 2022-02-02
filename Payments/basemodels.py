from pydantic import BaseModel


class Payload(BaseModel):
    ride_id: str= ""