from datetime import datetime, timedelta
from decimal import Decimal

from flask import Blueprint, request

from forms.order_forms import CreateOrderForm
from models.order import OrderLine
from services import order_service

bp_order = Blueprint('order', __name__)

__API_PREFIX__ = "/order"


@bp_order.route(f"{__API_PREFIX__}/create", methods=['POST'])
def create_order():
    body = request.get_json()
    form = CreateOrderForm(data=body)

    if not form.validate():
        return {"success": False, "errors": form.errors}, 400
    else:
        # 显式转换 total 为 Decimal
        body["total"] = Decimal(str(body["total"]))
        # 将普通字典列表 List[dict] 转为对象列表 List[OrderLine]
        order_lines = [
            OrderLine(
                cost=Decimal(str(order_line["cost"])),
                price=Decimal(str(order_line["price"])),
                product=order_line["product"],
                qty=order_line["qty"],
                sku=order_line["sku"]
            )
            for order_line in body["order_lines"]
        ]
        body["order_lines"] = order_lines
        order = order_service.create_one(**body)
        return {"success": True, "data": {"order": order}}, 200


@bp_order.route(f"{__API_PREFIX__}/<order_id>/info", methods=['GET'])
def get_order(order_id):
    order = order_service.find_one(order_id)
    return {"success": True, "data": {"order": order}}


@bp_order.route(f"{__API_PREFIX__}/count", methods=['GET'])
def count_orders():
    country = request.args.get("country", type=str, default=None)
    city = request.args.get("city", type=str, default=None)
    count = order_service.count_orders(country, city)
    return {"success": True, "data": count}


@bp_order.route(f"{__API_PREFIX__}/<int:user_id>/count", methods=['GET'])
def count_user_orders(user_id):
    count = order_service.count_user_orders(user_id)
    return {"success": True, "data": count}


@bp_order.route(f"{__API_PREFIX__}/getByTime", methods=['GET'])
def get_orders_by_time():
    # 获取时间戳
    start_time = request.args.get('start_time', type=int, default=None)
    end_time = request.args.get('end_time', type=int, default=None)
    # 获取 UTC 时间并手动 +8h 得到 UTC+8 时间
    start_datetime = datetime.utcfromtimestamp(start_time) + timedelta(hours=8)
    end_datetime = datetime.utcfromtimestamp(end_time) + timedelta(hours=8)
    count = order_service.find_orders_by_time(start_datetime, end_datetime)
    return {"success": True, "data": count}, 200


@bp_order.route(f"{__API_PREFIX__}/page", methods=['GET'])
def page_orders():
    page_num = request.args.get('page_num', default=1, type=int)
    page_size = request.args.get('page_size', default=10, type=int)
    orders = order_service.page_orders(page_num, page_size)
    return {"success": True, "data": orders}, 200


@bp_order.route(f"{__API_PREFIX__}/<order_id>/lines", methods=['GET'])
def get_order_lines(order_id):
    order_lines = order_service.find_order_lines(order_id)
    # Decimal128 是 MongoDB 的特殊类型，需先通过 .to_decimal() 转为 Python 的 Decimal
    # 再进一步转为 float 或 str（金额类数据建议用 str 避免精度丢失）
    result_data = [
        {'cost': str(order_line.cost.to_decimal()), 'qty': order_line.qty, 'sku': order_line.sku,
         'product': order_line.product, 'price': str(order_line.price.to_decimal())}
        for order_line in order_lines
    ]
    return {"success": True, "data": result_data}, 200
