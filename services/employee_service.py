from config import mongo_connect
from models.employee import Employee


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
