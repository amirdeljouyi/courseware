from website import db
from website.mod_student.models import Student
from website.mod_professor.models import Professor

teachers_courses = db.Table('teachers-courses',
                            db.Column('teacher_id', db.Integer, db.ForeignKey(
                                'professor.id'), primary_key=True),
                            db.Column('course_id', db.Integer,
                                      db.ForeignKey('course.id'), primary_key=True))

students_courses = db.Table('students-courses',
                            db.Column('student_id', db.Integer, db.ForeignKey(
                                'student.id'), primary_key=True),
                            db.Column('course_id', db.Integer,
                                      db.ForeignKey('course.id'), primary_key=True))

class Slide(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))

    def toJSON(self):
        return {
            'id':self.id,
            'name': self.name,
            'url': self.url,
        }

class Term(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    courses = db.relationship('Course', backref='term', lazy='dynamic')

"""Homework contain deadline"""
"""Syllabus"""

class UploadedHomework(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(120), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    posts = db.relationship('Post', backref='course', lazy='dynamic')
    slides = db.relationship('Slide', backref='course', lazy='dynamic')
    uploadedhomework = db.relationship('UploadedHomework', backref='course', lazy='dynamic')
    teachers = db.relationship('Professor',
                               secondary=teachers_courses, backref='course', lazy='dynamic')
    students = db.relationship('Student',
                               secondary=students_courses, backref='course', lazy='dynamic')
    term_id = db.Column(db.Integer, db.ForeignKey('term.id'))
    title = db.Column(db.String(120), nullable=True)
    minor_title = db.Column(db.String(250), nullable=True)
    video_url = db.Column(db.String(120), nullable=True)
    about = db.Column(db.Text, nullable=True)
    syllabus = db.Column(db.Text, nullable=True)
    homework = db.Column(db.Text, nullable=True)
    resources = db.Column(db.Text, nullable=True)
    degree = db.Column(db.String(120), nullable=True)

    def toJSON(self):
        return {
            'id':self.id,
            'title': self.title,
            'term': self.term.year,
            'video_url':self.video_url,
            'about':self.about,
            'syllabus':self.syllabus,
            'homwork':self.homework,
            'resources':self.resources,
            'degree':self.degree
        }