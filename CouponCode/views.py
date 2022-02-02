from fastapi import APIRouter, Request, Response, status

from Uber.CouponCode.basemodels import Payload
from Uber.CouponCode.manager import Manager

coupon_router = APIRouter()


@coupon_router.get('/api/coupons')
async def list_all_coupons(request: Request):
    """
    This API lists all coupons
    """
    res = Manager().list()
    return res

@coupon_router.post('/api/coupons')
async def create_coupon(request: Request, payload: Payload):
    """
    This API adds a coupon
    """
    res = Manager().create(payload.code, payload.value_discount, payload.percent_discount)
    return res

@coupon_router.delete('/api/coupons/{coupon_id}')
async def delete_coupon(request: Request, coupon_id):
    """
    This API adds a coupon
    """
    res = Manager(coupon_id).delete()
    return res