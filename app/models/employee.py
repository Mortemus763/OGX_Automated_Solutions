from app.models.db import environment, SCHEMA, add_prefix_for_prod
from datetime import date
from app import db

class Employee(db.Model):
    __tablename__ = 'employees'
    
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(255))
    date_of_birth = db.Column(db.Date)
    date_joined = db.Column(db.Date, default=date.today)
    status = db.Column(db.String(20), default='Active')

    department_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('departments.id')))
    position_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('positions.id')))

    department = db.relationship('Department', back_populates='employees')
    position = db.relationship('Position', back_populates='employees')

    def to_dict(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
            "date_of_birth": str(self.date_of_birth),
            "date_joined": str(self.date_joined),
            "status": self.status,
            "department": self.department.name if self.department else None,
            "position": self.position.title if self.position else None
        }
