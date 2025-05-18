from app import db

class Employee(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(50))
    department = db.Column(db.String(50))
    date_joined = db.Column(db.Date)
    status = db.Column(db.String(20), default="Active")

    def to_dict(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "email": self.email,
            "role": self.role,
            "department": self.department,
            "date_joined": str(self.date_joined),
            "status": self.status
        }
