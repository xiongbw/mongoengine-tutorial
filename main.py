import services.employee_service as employee_service


def main():
    # 1. 添加记录
    new_emp = employee_service.hire_one('张三', '男', 'IT 部')
    print(f"The new employee {new_emp.name} id is {new_emp.id}")

    # 2. 获取所有记录
    all_employees = employee_service.get_all()
    for employees in all_employees:
        print(employees)

    # 3. 条件查询获取一条记录
    employee = employee_service.get_by_name('张三')
    print(employee)

    # 4. 更新字段
    employee_service.update_department(new_emp.id, '嗷嗷')

    # 5. 删除记录
    employee_service.fire_employee(new_emp.id)


if __name__ == "__main__":
    main()
