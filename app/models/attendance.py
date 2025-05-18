from app.models.db import environment, SCHEMA, add_prefix_for_prod
from app import db

class Attendance(db.Model):
    __tablename__ = 'attendances'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('employees.id')))
    date = db.Column(db.Date)
    clock_in = db.Column(db.Time)
    clock_out = db.Column(db.Time)

    employee = db.relationship('Employee', backref='attendances')
