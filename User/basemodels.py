from bson import ObjectId
from pydantic import BaseModel


class UserPayload(BaseModel):
    name: str = ""
    email: str = ""
    mobile: str = ""