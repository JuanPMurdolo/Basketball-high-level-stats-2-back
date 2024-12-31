from db import db

class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=True)
    city = db.Column(db.String(80), nullable=True)
    
    def __repr__(self):
        return f'<Team {self.name}>'