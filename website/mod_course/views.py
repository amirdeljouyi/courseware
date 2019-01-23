from flask import Blueprint, render_template, request, redirect, url_for
from website import db, app, allowed_file
from website.mod_course.models import Course, Term , UploadedHomework
from flask_login import login_required, current_user
from website.mod_auth.models import User, Authority
from flask import jsonify, json
from werkzeug.utils import secure_filename
import os
from website.mod_professor.models import Professor
from time import gmtime, strftime
from website.mod_news.models import Post

# Define the blueprint: 'news', set its url prefix: app.url/course
mod_course = Blueprint('course', __name__, url_prefix='/course')


@mod_course.route('/', methods=['GET', 'POST'])
def course():
    # courses = db.session.query(Course).order_by(Course.term.desc()).all()
    courses = db.session.query(Course).all()
    if (current_user.is_authenticated):
        admin = db.session.query(Authority).filter(
            Authority.name == "Admin").first()
        if admin in current_user.authorities:
            return render_template('course/list.html', courses=courses, auth=True, pageNum=4)
    return render_template('course/list.html', courses=courses, auth=False, pageNum=4)


@mod_course.route('/filter', methods=['POST'])
def filterCourse():
    year = int(request.form['year'])
    term = db.session.query(Term).filter(Term.year == year).first()
    courses = term.courses
    if (current_user.is_authenticated):
        admin = db.session.query(Authority).filter(
            Authority.name == "Admin").first()
        if admin in current_user.authorities:
             return render_template('course/list.html', courses=courses, auth=True, pageNum=4)
    return render_template('course/list.html', courses=courses, auth=False, pageNum=4)


@mod_course.route('/<courseid>', methods=['GET'])
@login_required
def getCourse(courseid):
    course = db.session.query(Course).filter(Course.id == courseid).first()
    admin = db.session.query(Authority).filter(
        Authority.name == "Admin").first()
    prof = db.session.query(Authority).filter(
        Authority.name == "Professor").first()
    stu = db.session.query(Authority).filter(
        Authority.name == "Student").first()
    if admin in current_user.authorities and prof in current_user.authorities:
        return render_template('course/detail.html', course=course, auth=True, enroll=True, subPageNum=1, pageNum=4)
    if admin in current_user.authorities and stu in current_user.authorities and course not in current_user.student.course:
        return render_template('course/detail.html', course=course, auth=True, enroll=False, subPageNum=1, pageNum=4)
    if (prof in current_user.authorities) and (course in current_user.professor.course):
        return render_template('course/detail.html', course=course, auth=True, enroll=True, subPageNum=1, pageNum=4)
    if stu in current_user.authorities and course in current_user.student.course:
        return render_template('course/detail.html', course=course, enroll=True, auth=False, subPageNum=1, pageNum=4)
    return render_template('course/detail.html', course=course, enroll=False, auth=False, subPageNum=1, pageNum=4)


@mod_course.route('/edit/<courseid>', methods=['GET', 'POST'])
@login_required
def editCourse(courseid):
    course = db.session.query(Course).filter(Course.id == courseid).first()
    if request.method == "POST":
        if request.form['title'] == '' or request.form['title'] == None:
            print('Not exists')
        else:
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['VIDEO_FOLDER'], filename))
                course.video_url = filename
            term = db.session.query(Term).filter(
            Term.year == request.form['term']).first()
            course.title = request.form['title']
            course.minor_title = request.form['minor_title']
            course.about = request.form['about']
            course.syllabus = request.form['syllabus']
            course.degree = request.form['degree']
            course.homework = request.form['homework']
            course.resources = request.form['resources']
            course.term = term
            if request.form['teacher'] != '':
                teacher = db.session.query(Professor).filter(
                    Professor.id == request.form['teacher']).first()
                course.teachers.extend([teacher])

            db.session.commit()
    return render_template('course/add&edit.html', course=course, pageNum=4)


@mod_course.route('/add', methods=['GET', 'POST'])
@login_required
def addCourse():
    if request.method == "POST":
        if request.form['title'] == '' or request.form['title'] == None:
            print('Not exists')
        else:
            file = request.files['file']
            # if user does not select file, browser also submit a empty part
            if file.filename == '':
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['VIDEO_FOLDER'], filename))
            term = db.session.query(Term).filter(
                Term.year == request.form['term']).first()
            c = Course(
                title=request.form['title'],
                minor_title=request.form['minor_title'],
                about=request.form['about'],
                video_url=filename,
                syllabus=request.form['syllabus'],
                degree=request.form['degree'],
                homework=request.form['homework'],
                resources=request.form['resources'],
                term=term
            )
            teacher = db.session.query(Professor).filter(
                Professor.id == request.form['teacher']).first()
            c.teachers.extend([teacher])

            db.session.add(c)
            db.session.commit()
    return render_template('course/add&edit.html', pageNum=4)


@mod_course.route('/delete/<courseid>', methods=['POST'])
@login_required
def deleteCourse(courseid):
    admin = db.session.query(Authority).filter(
        Authority.name == "Admin").first()
    if(admin):
        p = db.session.query(Course).filter(Course.id == courseid).first()
        db.session.delete(p)
        db.session.commit()
        courses = db.session.query(Course).all()
        return render_template('course/list.html', courses=courses, auth=True, pageNum=4)

@mod_course.route('/enroll/<courseid>', methods=['POST'])
@login_required
def enrollCourse(courseid):
    c = db.session.query(Course).filter(Course.id == courseid).first()
    c.students.extend([current_user.student])
    db.session.commit()
    return redirect(url_for('course.getCourse',courseid=courseid))

@mod_course.route('/<courseid>/addnews', methods=['GET', 'POST'])
@login_required
def addNews(courseid):
    c = db.session.query(Course).filter(Course.id == courseid).first()
    if request.method == "POST":
        if request.form['content'] == '' or request.form['content'] == None:
            print('Not exists')
        else:
            file = request.files['file']
            # if user does not select file, browser also submit a empty part
            if file.filename == '':
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['IMG_FOLDER'], filename))

            p = Post(
                title=request.form['title'],
                user=current_user,
                content=request.form['content'],
                date=strftime("%Y-%m-%d %H:%M:%S", gmtime()),
                img_url=filename,
                course=c
            )

            db.session.add(p)
            db.session.commit()

    return render_template('course/add-news.html',course=c)

@mod_course.route('/<courseid>/upload-homework', methods=['GET', 'POST'])
@login_required
def uploadHomework(courseid):
    stu = db.session.query(Authority).filter(
        Authority.name == "Student").first()
    course = db.session.query(Course).filter(Course.id == courseid).first()
    if stu in current_user.authorities and course in current_user.student.course:
        if request.method == "POST":
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['HOMEWORK_FOLDER'], filename))
                u = UploadedHomework(
                    url="filename",
                    course=course,
                    student=current_user.student
                )
                db.session.add(u)
                db.session.commit()

        return render_template('course/upload-homework.html', course=course, pageNum=4)