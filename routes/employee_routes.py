from flask import Blueprint, request

from forms.employee_forms import DepartmentForm, HireEmployeeForm
from services import employee_service

bp_employee = Blueprint('employee', __name__)

__API_PREFIX__ = "/employee"


@bp_employee.route(f"{__API_PREFIX__}/hire", methods=['POST'])
def hire_employee():
    body = request.get_json()
    form = HireEmployeeForm(data=body)

    if not form.validate():
        return {"success": False, "errors": form.errors}, 400
    else:
        emp = employee_service.hire_one(**body)
        result_data = {'id': str(emp.id), 'name': emp.name, 'gender': emp.gender, 'department': emp.department}
        return {"success": True, "data": result_data}, 200


@bp_employee.route(f"{__API_PREFIX__}/list", methods=['GET'])
def all_employees():
    employee_list = employee_service.get_all()
    employees = [
        {'id': str(emp.id), 'name': emp.name, 'gender': emp.gender, 'department': emp.department}
        for emp in employee_list
    ]
    return {"employees": employees}


@bp_employee.route(f"{__API_PREFIX__}/<emp_id>/info", methods=['GET'])
def get_employee_by_id(emp_id):
    employee = employee_service.get_by_id(emp_id)
    if employee:
        return {'employee': {'name': employee.name, 'gender': employee.gender, 'department': employee.department}}
    else:
        return {'employee': {}}


@bp_employee.route(f"{__API_PREFIX__}/<emp_id>/updateDept", methods=['POST'])
def update_department(emp_id):
    body = request.get_json()
    form = DepartmentForm(data=body)

    if not form.validate():
        return {"success": False, "errors": form.errors}, 400
    else:
        employee_service.update_department(emp_id, **body)
        return {"success": True}, 200


@bp_employee.route(f"{__API_PREFIX__}/getByName", methods=['GET'])
def get_employees_by_name():
    name = request.args['name']
    employee_list = employee_service.get_by_name(name)
    employees = [
        {'id': str(emp.id), 'name': emp.name, 'gender': emp.gender, 'department': emp.department}
        for emp in employee_list
    ]
    return {"employees": employees}
