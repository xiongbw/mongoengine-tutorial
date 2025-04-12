import mongoengine as db
from mongoengine import EmbeddedDocumentField, EmbeddedDocument


class OrderLine(EmbeddedDocument):
    """
    订单项
    """
    # 成本
    cost = db.Decimal128Field()
    # 价格
    price = db.Decimal128Field()
    # 产品
    product = db.StringField()
    # Quantity（数量）
    qty = db.IntField()
    # Stock Keeping Unit（库存量单位）
    sku = db.StringField()

    def __init__(self, cost, price, product, qty, sku, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cost = cost
        self.price = price
        self.product = product
        self.qty = qty
        self.sku = sku

    def __str__(self):
        return f"cost: {self.cost}, price: {self.price}, product: {self.product}, qty: {self.qty}"


class Order(db.Document):
    """
    订单
    """
    # 城市
    city = db.StringField()
    # 国家
    country = db.StringField()
    # 创建日期
    create_time = db.DateTimeField(db_field='createTime')
    # 是否删除
    is_deleted = db.BooleanField(db_field='isDeleted')
    # 名称
    name = db.StringField()
    # 订单日期
    order_date = db.DateTimeField(db_field='orderDate')
    # 电话号码
    phone = db.StringField()
    # 邮费
    shipping_fee = db.Decimal128Field(db_field='shippingFee')
    # 州
    state = db.StringField()
    # 状态
    status = db.StringField()
    # 街道
    street = db.StringField()
    # 总金额
    total = db.Decimal128Field()
    # 更新日期
    update_time = db.DateTimeField(db_field='updateTime')
    # 用户 ID
    user_id = db.IntField(db_field='userId')
    # Zone Improvement Plan code（美国邮政编码）
    zip = db.StringField()
    # 订单详情（嵌入文档）
    order_lines = db.ListField(EmbeddedDocumentField(OrderLine), db_field='orderLines')

    meta = {
        'collection': 'order'
    }

    def __init__(self, city, country, create_time, is_deleted, name, order_date, phone, shipping_fee,
                 state, status, street, total, update_time, user_id, zip, order_lines, *args, **values):
        super().__init__(*args, **values)
        self.city = city
        self.country = country
        self.create_time = create_time
        self.is_deleted = is_deleted
        self.name = name
        self.order_date = order_date
        self.phone = phone
        self.shipping_fee = shipping_fee
        self.state = state
        self.status = status
        self.street = street
        self.total = total
        self.update_time = update_time
        self.user_id = user_id
        self.zip = zip
        self.order_lines = order_lines

    def __str__(self):
        return f"{self.id}, {self.city}, {self.country}, {self.name}, {self.state}, {self.city}, {self.country}, {self.update_time}, {self.user_id}, {self.zip}, {self.state}, {self.total}, {self.order_lines}"
