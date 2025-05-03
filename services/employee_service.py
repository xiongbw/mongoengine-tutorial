from typing import List

from bson import ObjectId

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


def get_by_id(emp_id: str) -> Employee:
    """
    Get employee by id
    :param emp_id: employee id
    :return: Employee object if exists
    """
    if not ObjectId.is_valid(emp_id):
        return None
    else:
        return Employee.objects(id=emp_id).first()

