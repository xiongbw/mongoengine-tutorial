import services.employee_service as employee_service


def main():
    # 1. 添加记录
    new_emp = employee_service.hire_one('张三', '男', 'IT 部')
    print(f"The new employee {new_emp.name} id is {new_emp.id}")

    # 2. 获取所有记录
    all_employees = employee_service.get_all()
    for employees in all_employees:
        print(employees)


if __name__ == "__main__":
    main()
