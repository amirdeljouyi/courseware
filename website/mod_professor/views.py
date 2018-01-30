from flask import render_template, request, redirect, url_for, Blueprint
from website import mod_professor, db
from website.mod_professor.models import Professor
from website.mod_news.models import Post
from website.mod_auth.models import User
from flask_login import current_user
from website.mod_auth.models import User
from website.mod_auth.views import login_required
from werkzeug.security import generate_password_hash
from website.mod_auth.models import User, Authority


mod_professor = Blueprint('professor', __name__, url_prefix='/professor')


@mod_professor.route('/')
def faculty():
    professors = db.session.query(Professor).all()
    if current_user.is_authenticated:
        if current_user.isAdmin():
            return render_template('professor/list.html', professors=professors, auth=True, pageNum=5)
    return render_template('professor/list.html', professors=professors, auth=False, pageNum=5)


@mod_professor.route('/add', methods=['GET', 'POST'])
@login_required(role="Admin")
def addProfessor():
    if request.method == "POST":
        if request.form['username'] == '' or request.form['password'] == '':
            print('Not exists')
        else:
            p = Professor(
                field_of_study=request.form['field_of_study'],
                degree=request.form['degree'],
                level=request.form['level'],
            )
            u = User(
                first_name=request.form['firstname'],
                last_name=request.form['lastname'],
                username=request.form['username'],
                password_hash=generate_password_hash(request.form['password']),
                professor=p,
                verify=True
            )
            pA = db.session.query(Authority).filter(
                Authority.name == "Professor").first()
            u.authorities.append(pA)
            db.session.add_all([p, u])
            db.session.commit()
    return render_template('professor/add&edit.html')


@mod_professor.route('/edit/<professorid>', methods=['GET', 'POST'])
@login_required(role="Admin")
def editProfessor(professorid):
    p = db.session.query(Professor).filter(Professor.id == professorid).first()
    if request.method == "POST":
        p.user.first_name = request.form['firstname']
        p.user.last_name = request.form['lastname']
        p.user.username = request.form['lastname']
        p.level = request.form['level']
        p.degree = request.form['degree']
        p.field_of_study = request.form['field_of_study']
        if request.form['password'] != None:
            p.user.password_hash = generate_password_hash(
                request.form['password'])
        print(p)
        db.session.commit()
    return render_template('professor/add&edit.html', professor=p)


@mod_professor.route('/delete/<professorid>', methods=['POST'])
@login_required(role="Admin")
def deleteProfessor(professorid):
    p = db.session.query(Professor).filter(Professor.id == professorid).first()
    db.session.delete(p)
    db.session.commit()
    professors = db.session.query(Professor).all()
    return render_template('professor/list.html', professors=professors, auth=True, pageNum=5)
