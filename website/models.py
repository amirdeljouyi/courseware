from website import db

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.relationship('User', backref='professor',
                           uselist=False)
    field_of_study = db.Column(db.String(100), nullable=True)
    degree = db.Column(db.String(30), nullable=True)
    level = db.Column(db.String(30), nullable=True)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.relationship('User', backref='student',
                           uselist=False)
    year_of_enter = db.Column(db.Integer, nullable=True)
    field_of_study = db.Column(db.String(100), nullable=True)
    degree = db.Column(db.String(30), nullable=True)