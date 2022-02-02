from fastapi import APIRouter, Request, Response, status

from Uber.Payments.basemodels import Payload
from Uber.Payments.manager import Manager

payments_router = APIRouter()


@payments_router.get('/api/payments')
async def list_all_transactions(request: Request):
    """
    This API lists all transactions
    """
    res = Manager().list()
    return res

# @payments_router.post('/api/payment')
# async def create_transaction(request: Request, payload: Payload):
#     """
#     This API adds a transaction
#     """
#     res = Manager().create(payload.code, payload.value_discount, payload.percent_discount)
#     return res