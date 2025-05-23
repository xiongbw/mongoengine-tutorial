from decimal import Decimal
from datetime import datetime
from typing import List

from bson import ObjectId

from config import mongo_connect
from constants.order_status_enums import OrderStatusEnum
from models.order import Order, OrderLine


def create_one(city: str, country: str, name: str, phone: str, shipping_fee: Decimal, state: str, street: str,
               total: Decimal, user_id: int, zip: str, order_lines: List[OrderLine]) -> Order:
    """
    创建订单
    :param city: 城市
    :param country: 国家
    :param name: 名称
    :param phone: 电话号码
    :param shipping_fee: 邮费
    :param state: 州
    :param street: 街道
    :param total: 总金额
    :param user_id: 用户 ID
    :param zip: 邮政编码
    :param order_lines: 订单详情
    :return: Order object
    """
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


def count_orders(country: str = None, city: str = None) -> int:
    """
    统计订单数量
    :param country: 国家
    :param city: 城市
    :return: Order count
    """
    query_filter = {'is_deleted': False}
    if country and country.strip():
        query_filter['country'] = country
    if city and city.strip():
        query_filter['city'] = city

    return Order.objects(**query_filter).count()


def count_user_orders(user_id: int) -> int:
    """
    统计用户订单数量
    :param user_id: 用户 ID
    :return: Order count
    """
    return Order.objects(user_id=user_id, is_deleted=False).count()


def find_orders_by_time(start_time: datetime, end_time: datetime) -> List[Order]:
    """
    通过创建时间查询订单
    :param start_time: 开始时间
    :param end_time: 结束时间
    :return: Order List
    """
    return Order.objects(create_time__gte=start_time, create_time__lte=end_time, is_deleted=False)


def page_orders(page_num: int = 1, page_size: int = 5) -> List[Order]:
    """
    分页查询订单
    :param page_num: 页码
    :param page_size: 页面大小
    :return: 页面订单列表
    """
    offset = (page_num - 1) * page_size
    return Order.objects(is_deleted=False).skip(offset).limit(page_size)


def find_order_lines(order_id: Order.id) -> List[OrderLine]:
    """
    获取订单项列表
    :param order_id: 订单 ID
    :return: List[dict] with OrderLines
    """
    if not ObjectId.is_valid(order_id):
        return []

    pipeline = [
        {'$match': {'_id': ObjectId(order_id), 'isDeleted': False}},
        {'$project': {'_id': 0, 'orderLines': 1}},
    ]
    results = Order.objects().aggregate(pipeline)
    order = next(results, None)
    # -> List[dict]
    # return order['orderLines'] if order else []
    return [OrderLine(**line) for line in order['orderLines']] if order else []


def count_city_orders():
    """
    统计城市订单数量
    :return: Order quantity for all cities
    """
    pipeline = [
        {'$match': {'isDeleted': False}},
        {'$group': {'_id': '$city', 'count': {'$sum': 1}}},
        {'$project': {'city': '$_id', 'count': '$count'}},
    ]
    return Order.objects().aggregate(pipeline)
