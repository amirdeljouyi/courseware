from website import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.relationship('User', backref='student',
                           uselist=False)
    year_of_enter = db.Column(db.Integer, nullable=True)
    field_of_study = db.Column(db.String(100), nullable=True)
    degree = db.Column(db.String(30), nullable=True)
    uploadedhomework = db.relationship('UploadedHomework', backref='student', lazy='dynamic')