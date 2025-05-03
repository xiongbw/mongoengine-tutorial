from wtforms import Form, StringField
from wtforms.validators import DataRequired, AnyOf


class DepartmentForm(Form):
    """
    Form for setting a department
    """
    department = StringField(label='部门', validators=[DataRequired(message="请指定部门")])


class NameForm(Form):
    """
    Form for setting a name
    """
    name = StringField(label='姓名', validators=[DataRequired(message='请输入姓名')])


class HireEmployeeForm(DepartmentForm, NameForm):
    """
    Form for hiring an employee
    """
    gender = StringField(label='性别', validators=[
        DataRequired(message="请指定性别"),
        AnyOf(['男', '女'], message='性别必须是“男”或“女”')
    ])
