from wtforms import Form, StringField, IntegerField
from wtforms.fields.form import FormField
from wtforms.fields.list import FieldList
from wtforms.fields.numeric import DecimalField
from wtforms.validators import DataRequired, NumberRange, Optional


class OrderLineForm(Form):
    # DecimalField 的核心作用：将输入值转换为符合指定小数位数的 Decimal 对象，而非严格校验位数。
    # 当传入 9.1234 且 places=2 时，会将其自动处理为 9.12（截断）或 9.12（四舍五入，取决于 rounding 参数），并不会触发验证错误。
    cost = DecimalField('成本', places=2, validators=[
        DataRequired(message="请指定成本"),
        NumberRange(min=0, message="成本不能为负数")
    ])
    price = DecimalField('价格', places=2, validators=[
        DataRequired(message="请指定价格"),
        NumberRange(min=0, message="价格不能为负数")
    ])
    product = StringField('产品名称', validators=[DataRequired(message='请指定产品名称')])
    qty = IntegerField('数量', validators=[
        DataRequired(message='请指定产品数量'),
        NumberRange(min=1, message='产品数量至少为 %(min)d')
    ])
    sku = StringField('库存量单位', validators=[DataRequired(message='请指定库存量单位')])


class CreateOrderForm(Form):
    city = StringField('城市', validators=[DataRequired(message='请指定城市')])
    country = StringField('国家', validators=[DataRequired(message='请指定国家')])
    name = StringField('名称', validators=[DataRequired(message='请输入名称')])
    phone = StringField('电话号码', validators=[DataRequired(message='请输入电话号码')])
    shipping_fee = DecimalField('邮费', validators=[
        Optional(),
        NumberRange(min=0, message='邮费不能为负数')
    ])
    state = StringField('州', validators=[DataRequired(message='请指定州')])
    street = StringField('街道', validators=[DataRequired(message='请指定街道')])
    total = DecimalField('总金额', places=2, validators=[
        DataRequired(message="请指定总金额"),
        NumberRange(min=0.00, message="总金额不能为负数")
    ])
    user_id = IntegerField('用户 ID', validators=[DataRequired(message='请指定用户 ID')])
    zip = StringField('美国邮政编码')
    order_lines = FieldList(FormField(OrderLineForm), validators=[DataRequired(message='订单项不能为空')])
