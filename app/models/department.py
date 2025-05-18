from app.models.db import environment, SCHEMA
from app import db

class Department(db.Model):
    __tablename__ = 'departments'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(255))

    employees = db.relationship('Employee', back_populates='department')
