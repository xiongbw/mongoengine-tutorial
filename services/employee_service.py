from bson import ObjectId

from config import mongo_connect
from models.employee import Employee
from mongoengine import DoesNotExist, MultipleObjectsReturned


def hire_one(name, gender, department):
    """
    录用员工
    :param name: the employee name
    :param gender: the employee gender
    :param department: the employee department
    :return: Employee object
    """
    employee = Employee(name=name, gender=gender, department=department)
    employee.save()
    return employee


def get_all():
    """
    :return: All employees
    """
    return Employee.objects.all()


def get_by_name(name):
    """
    通过姓名获取员工
    get() -> 必须获取有且仅有一条符合条件的数据
    first() -> 获取第一条符合条件的数据，没有则返回 None
    :param name: the employee name
    :return: Employee object
    """
    # try:
    #     return query_set.get()
    # except DoesNotExist:
    #     print(f"No employee with name '{name}'")
    #     return None
    # except MultipleObjectsReturned:
    #     print(f"Multiple employees with name '{name}'")
    #     return None
    query_set = Employee.objects(name=name)
    return query_set.first()


def update_department(emp_id, department):
    """
    更改部门
    :param emp_id: the employee id
    :param department: department name
    """
    if not ObjectId.is_valid(emp_id):
        return None

    query_set = Employee.objects(id=emp_id)
    if query_set.count() > 0:
        query_set.update_one(department=department)
