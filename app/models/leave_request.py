from app.models.db import environment, SCHEMA, add_prefix_for_prod
from app import db

class LeaveRequest(db.Model):
    __tablename__ = 'leave_requests'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('employees.id')))
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    reason = db.Column(db.String(255))
    status = db.Column(db.String(20), default='Pending')

    employee = db.relationship('Employee', backref='leave_requests')
