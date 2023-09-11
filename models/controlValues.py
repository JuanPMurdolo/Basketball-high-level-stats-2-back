from db import db

class ControlValues(db.Model):
    __tablename__ = "control_values"
    id = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    value = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return f"<ControlValues {self.name}>"