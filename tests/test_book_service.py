import unittest

import services.employee_service as employee_service


class TestEmployeeService(unittest.TestCase):

    def test_hire_one(self):
        new_emp = employee_service.hire_one('张三', '男', 'IT 部')
        print(f"The new employee {new_emp.name} id is {new_emp.id}")

    def test_get_all(self):
        all_employees = employee_service.get_all()
        for employee in all_employees:
            print(employee)

    def test_get_by_name(self):
        employee = employee_service.get_by_name('张三')
        print(employee)

    def test_update_department(self):
        employee_service.update_department("67ed2ef4a861513f94fc49af", '财务部')

    def test_fire_employee_valid_id(self):
        employee_service.fire_employee("67ed2f218c8e329727a008bd")


if __name__ == '__main__':
    unittest.main()
