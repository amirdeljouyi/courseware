from flask import Blueprint, render_template, request, redirect, url_for
from website import db
from website.mod_course.models import Course
from flask_login import login_required

# Define the blueprint: 'news', set its url prefix: app.url/course
mod_course = Blueprint('course', __name__, url_prefix='/course')


@mod_course.route('/')
def course():
    courses = db.session.query(Course).all()
    return render_template('course/list.html', courses=courses, pageNum=4)


@mod_course.route('/<courseid>')
@login_required
def showCourse(courseid):
    course = db.session.query(Course).filter(Course.id == courseid).first()
    return render_template('course/detail.html', course=course, subPageNum=1, pageNum=4)


@mod_course.route('/<courseid>/resources')
@login_required
def showCourseResources(courseid):
    course = db.session.query(Course).filter(Course.id == courseid).first()
    return render_template('course/detail.resources.html', course=course, subPageNum=2, pageNum=4)


@mod_course.route('/<courseid>/syllabus')
@login_required
def showCourseSyllabus(courseid):
    course = db.session.query(Course).filter(Course.id == courseid).first()
    return render_template('course/detail.syllabus.html', course=course, subPageNum=3, pageNum=4)


@mod_course.route('/<courseid>/slides')
@login_required
def showCourseSlides(courseid):
    course = db.session.query(Course).filter(Course.id == courseid).first()
    slides = course.slides
    return render_template('course/detail.slides.html', course=course, slides=slides, subPageNum=4, pageNum=4)


@mod_course.route('/<courseid>/homework')
@login_required
def showCourseHomework(courseid):
    course = db.session.query(Course).filter(Course.id == courseid).first()
    return render_template('course/detail.homework.html', course=course, subPageNum=5, pageNum=4)


@mod_course.route('/<courseid>/news')
@login_required
def showCourseNews(courseid):
    course = db.session.query(Course).filter(Course.id == courseid).first()
    posts = course.posts
    return render_template('course/detail.news.html', course=course, posts=posts, subPageNum=6, pageNum=4)
