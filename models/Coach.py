from db import db

class Coach(db.Model):
    __tablename__ = 'coaches'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    teams = db.Column(db.String(80), nullable=True)

    def __repr__(self):
        return f'<Coach {self.name}>'