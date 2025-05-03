from datetime import datetime
from decimal import Decimal
from typing import List

from bson import ObjectId

from constants.order_status_enums import OrderStatusEnum
from models.order import Order, OrderLine


def create_one(city: str, country: str, name: str, phone: str, state: str, street: str,
               total: Decimal, user_id: int, order_lines: List[OrderLine],
               shipping_fee: Decimal = None, zip: str = '') -> Order:
    """
    创建订单
    :param city: 城市
    :param country: 国家
    :param name: 名称
    :param phone: 电话号码
    :param state: 州
    :param street: 街道
    :param total: 总金额
    :param user_id: 用户 ID
    :param order_lines: 订单详情
    :param shipping_fee: 邮费
    :param zip: 邮政编码
    :return: Order object
    """
    if shipping_fee is None:
        shipping_fee = Decimal('0.00')
    if zip is None:
        zip = ''
    now = datetime.now()
    order = Order(city, country, now, False, name, now, phone, shipping_fee, state,
                  OrderStatusEnum.CREATED.value, street, total, now, user_id, zip, order_lines)
    return order.save()


def find_one(order_id: Order.id):
    """
    获取订单
    :param order_id: 订单 ID
    :return: Order object
    """
    if not ObjectId.is_valid(order_id):
        return None

    return Order.objects(id=order_id, is_deleted=False).first()
