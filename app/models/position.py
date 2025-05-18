from app.models.db import environment, SCHEMA
from app import db

class Position(db.Model):
    __tablename__ = 'positions'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))

    employees = db.relationship('Employee', back_populates='position')
