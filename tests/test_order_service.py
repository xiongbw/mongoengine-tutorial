from datetime import datetime
from decimal import Decimal
import unittest

from models.order import OrderLine
from services import order_service


class TestOrderService(unittest.TestCase):

    def test_add_one(self):
        city = "Klington"
        country = "Belgium"
        name = "Cathryn Langosh"
        phone = "(216) 394-6317"
        shipping_fee = Decimal("5")
        state = "Colorado"
        street = "1674 Schumm Camp"
        total = Decimal("435")
        user_id = 1031
        zip = "37146"

        order_line1 = {
            "product": "Intelligent Concrete Computer", "sku": "2715", "qty": 92,
            "price": Decimal("90.00"), "cost": Decimal("72.9")
        }
        order_line2 = {
            "product": "Incredible Wooden Chair", "sku": "202", "qty": 45,
            "price": Decimal("77.00"), "cost": Decimal("70.84")
        }
        order_lines = [OrderLine(**order_line1), OrderLine(**order_line2)]
        order = order_service.create_one(city, country, name, phone, shipping_fee, state, street, total, user_id, zip,
                                         order_lines)
        print(order)

    def test_find_one(self):
        order_id = "67f0e8dfb889cbfa4377388c"
        order = order_service.find_one(order_id)
        print(order)

    def test_count_orders(self):
        country = "China"
        city = "Shenzhen"
        count = order_service.count_orders(country, city)
        print(f"In {country} {city} has {count} orders")

    def test_count_user_orders(self):
        user_id = 123
        count = order_service.count_user_orders(user_id)
        print(f"User {user_id} has {count} orders")

    def test_find_orders_by_time(self):
        start_time = datetime(2024, 10, 15, 14, 30, 0)
        end_time = datetime(2025, 10, 15, 14, 30, 0)
        orders = order_service.find_orders_by_time(start_time, end_time)
        for order in orders:
            print(order)

    def test_page_orders(self):
        total_count = order_service.count_orders()
        print(f"Total orders: {total_count}")
        if total_count == 0:
            return None

        page_size = 3
        total_pages = (total_count + page_size - 1) // page_size
        for page_num in range(1, total_pages + 1):
            orders = order_service.page_orders(page_num, page_size)
            for order in orders:
                print(order)

    def test_find_order_lines(self):
        order_lines = order_service.find_order_lines("67f521c453c37e631d447575")
        for order_line in order_lines:
            print(order_line)

    def test_count_city_orders(self):
        city_orders_count = order_service.count_city_orders()
        if city_orders_count:
            for orders_count in city_orders_count:
                print(f"City {orders_count['city']} has {orders_count['count']} orders.")


if __name__ == '__main__':
    unittest.main()
