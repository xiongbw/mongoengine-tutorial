from enum import Enum


class OrderStatusEnum(Enum):
    """
    订单状态枚举
    """
    # 已创建
    CREATED = "created"
    # 已处理
    FULFILLED = "fulfilled"
    # 运输中
    SHIPPING = "shipping"
    # 已完成
    COMPLETED = "completed"
    # 已取消
    CANCELLED = "cancelled"
