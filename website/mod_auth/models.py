from website import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

authorities_users = db.Table('authorities-users',
                             db.Column('authority_id', db.Integer, db.ForeignKey(
                                 'authority.id'), primary_key=True),
                             db.Column('user_id', db.Integer,
                                       db.ForeignKey('user.id'), primary_key=True))

class Authority(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    authorities = db.relationship('Authority',
                                  secondary=authorities_users, backref='user', lazy='dynamic')
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(120), nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    img_url = db.Column(db.String(120), nullable=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'))
    posts = db.relationship('Post', backref='user', lazy='dynamic')
    verify = db.Column(db.Boolean,nullable=False)

    def isAdmin(self):
        for auth in self.authorities:
            if auth.name == "Admin":
                return True
        return False

    def isStudent(self):
        for auth in self.authorities:
            if auth.name == "Student":
                return True
        return False

    def isProfessor(self):
        for auth in self.authorities:
            if auth.name == "Professor":
                return True
        return False

    def isHaveRole(self,role):
        for auth in self.authorities:
            if auth.name == role:
                return True
        return False

    @property
    def password(self):
        raise AttributeError('password: write-only field')
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)