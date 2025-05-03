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
