from pydantic import BaseModel


class Payload(BaseModel):
    code: str = ""
    value_discount: int = 0
    percent_discount: int = 0