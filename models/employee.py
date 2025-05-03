from . import db


class Employee(db.Document):
    name = db.StringField()
    gender = db.StringField()
    department = db.StringField()

    meta = {
        'collection': 'employee',
        'db_alias': 'standalone'
    }
