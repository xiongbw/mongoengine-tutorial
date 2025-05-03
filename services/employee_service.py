from typing import List

from models.employee import Employee


def hire_one(department: str, name: str, gender: str) -> Employee:
    """
    录用员工
    :param name: the employee name
    :param gender: the employee gender
    :param department: the employee department
    :return: Employee object
    """
    employee = Employee(name=name, gender=gender, department=department)
    return employee.save()


def get_all() -> List[Employee]:
    """
    :return: All employees
    """
    return Employee.objects.all()
