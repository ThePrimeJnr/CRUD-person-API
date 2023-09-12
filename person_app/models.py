from . import db

class Person(db.Model):
    __tablename__ = 'persons'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def to_json(self):
        return {
            'isbn': self.user_id,
            'name': self.name
        }

