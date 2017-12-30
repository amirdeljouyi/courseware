from website import db


class Slide(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    posts = db.relationship('Post', backref='course', lazy='dynamic')
    slides = db.relationship('Slide', backref='course', lazy='dynamic')
    title = db.Column(db.String(120), nullable=True)
    about = db.Column(db.Text, nullable=True)
    year = db.Column(db.Integer, nullable=False)
    syllabus = db.Column(db.Text, nullable=True)
    homework = db.Column(db.Text, nullable=True)
    resources = db.Column(db.Text, nullable=True)
    degree = db.Column(db.String(120), nullable=True)
