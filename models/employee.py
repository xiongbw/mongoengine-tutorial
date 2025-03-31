import mongoengine as db


class Employee(db.Document):
    name = db.StringField()
    gender = db.StringField()
    department = db.StringField()

    meta = {
        'collection': 'employee'
    }

    def __str__(self):
        return f"{self.id}: {self.name} - {self.gender} - {self.department}"
