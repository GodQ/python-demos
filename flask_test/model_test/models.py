from app_init import db


class Test(db.Model):
    name = db.Column(db.String(20), primary_key=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def delete_by_name(cls, name):
        inst = Test.query.filter_by(name=name).first()
        db.session.delete(inst)
        db.session.commit()

    def delete(self):
        Test.delete_by_name(self.name)

    @classmethod
    def delete_all(cls):
        for t in Test.query.all():
            t.delete()
