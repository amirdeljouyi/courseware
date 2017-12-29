from flask import Blueprint , render_template, request, redirect, url_for
from website import app, db
from website.models import  Student, Professor
from website.mod_auth.models import User, Authority
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

@mod_auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        if request.form['username'] == '' or request.form['username'] == None:
            print('Not exists')
            redirect(url_for('login'))
        if request.form['password'] == '' or request.form['password'] == None:
            print('Not exists')
            redirect(url_for('login'))
        user = db.session.query(User).filter_by(
            username=request.form['username']).first()
        if user is not None and user.check_password(request.form['password']):
            login_user(user)
            return redirect(url_for('index')) or url_for('index')
    return render_template('auth/login.html', pageNum=0)


@mod_auth.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('index'))


@mod_auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        if request.form['username'] == '' or request.form['username'] == None:
            print('Not exists')
            redirect(url_for('register'))
        if request.form['password'] == '' or request.form['password'] == None:
            print('Not exists')
            redirect(url_for('register'))
        if request.form['password'] != request.form['confirm_password']:
            print('Passwords is not equal')
            redirect(url_for('register'))
        user = db.session.query(User).filter_by(
            username=request.form['username']).first()
        if user is not None:
            print('User is exist')
            redirect(url_for('login'))

        if request.form['authority'] == "student":
            authorityStudent = Authority(
                name="Student"
            )
            s = Student()
            u = User(
                username=request.form['username'],
                first_name=request.form['firstname'],
                last_name=request.form['lastname'],
                password_hash=generate_password_hash(request.form['password']),
                student=s
            )
            u.authorities.append(authorityStudent)
            db.session.add(s)

        elif request.form['authority'] == "professor":
            authorityProfessor = Authority(
                name="Professor"
            )
            p = Professor()
            u = User(
                username=request.form['username'],
                first_name=request.form['firstname'],
                last_name=request.form['lastname'],
                password_hash=generate_password_hash(request.form['password']),
                professor=p
            )
            u.authorities.append(authorityProfessor)
            db.session.add(p)

        db.session.add(u)
        db.session.commit()
        login_user(u)
        return redirect(url_for('index')) or url_for('index')

    return render_template('auth/register.html', pageNum=0)
