from flask import render_template, request, redirect, url_for, Blueprint
from website import app, db
from website.mod_student.models import Student
from website.mod_news.models import Post
from website.mod_auth.models import User, Authority
from website.mod_auth.views import login_required
from flask_login import current_user
from website.mod_auth.models import User, Authority
from werkzeug.security import generate_password_hash


mod_student = Blueprint('student', __name__, url_prefix='/student')


@mod_student.route('/')
def student():
    students = db.session.query(Student).all()
    if current_user.is_authenticated:
        if current_user.isAdmin():
            return render_template('student/list.html', students=students, auth=True, subPageNum=1, pageNum=3)
    return render_template('student/list.html', students=students, auth=False, subPageNum=1, pageNum=3)


@mod_student.route('/add', methods=['GET', 'POST'])
@login_required(role="Admin")
def addStudent():
    if request.method == "POST":
        if request.form['username'] == '' or request.form['password'] == '':
            print('Not exists')
        else:
            print("hi")
            student = Student(
                field_of_study=request.form['field_of_study'],
                degree=request.form['degree'],
                year_of_enter=request.form['year_of_enter'],
            )
            u = User(
                first_name=request.form['firstname'],
                last_name=request.form['lastname'],
                username=request.form['username'],
                password_hash=generate_password_hash(request.form['password']),
                student=student,
                verify=True
            )
            sA = db.session.query(Authority).filter(
                Authority.name == "Student").first()
            u.authorities.append(sA)
            db.session.add_all([student, u])
            db.session.commit()
    return render_template('student/add&edit.html')


@mod_student.route('/edit/<studentid>', methods=['GET', 'POST'])
@login_required(role="Admin")
def editStudent(studentid):
    p = db.session.query(Student).filter(Student.id == studentid).first()
    if request.method == "POST":
        p.user.first_name = request.form['firstname']
        p.user.last_name = request.form['lastname']
        p.user.username = request.form['username']
        p.year_of_enter = request.form['year_of_enter']
        p.degree = request.form['degree']
        p.field_of_study = request.form['field_of_study']
        if request.form['password'] != None:
            p.user.password_hash = generate_password_hash(
                request.form['password'])
        db.session.commit()
    return render_template('student/add&edit.html', student=p)


@mod_student.route('/delete/<studentid>', methods=['POST'])
@login_required(role="Admin")
def deleteStudent(studentid):
    p = db.session.query(Student).filter(Student.id == studentid).first()
    db.session.delete(p)
    db.session.commit()
    students = db.session.query(Student).all()
    return render_template('student/list.html', students=students, auth=True, pageNum=5)
