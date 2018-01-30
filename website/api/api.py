from flask import Blueprint, jsonify, json
from website import db
from website.mod_course.models import Course, Term

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/course/<courseid>', methods=['GET'])
def getCourse(courseid):
    course = db.session.query(Course).filter(Course.id == courseid).first()
    return jsonify(course.toJSON())

@api.route('/course/<courseid>/resources', methods=['GET'])
def getResources(courseid):
    course = db.session.query(Course).filter(Course.id == courseid).first()
    return jsonify(course.resources)


@api.route('/course/<courseid>/syllabus', methods=['GET'])
def getSyllabus(courseid):
    course = db.session.query(Course).filter(Course.id == courseid).first()
    return jsonify(course.syllabus)


@api.route('/course/<courseid>/slides', methods=['GET'])
def getSlides(courseid):
    course = db.session.query(Course).filter(Course.id == courseid).first()
    slides = course.slides
    jsonStr = json.dumps([e.toJSON() for e in slides])
    return jsonify(jsonStr)


@api.route('/course/<courseid>/homework', methods=['GET'])
def getHomework(courseid):
    course = db.session.query(Course).filter(Course.id == courseid).first()
    return jsonify(course.homework)


@api.route('/course/<courseid>/news', methods=['GET'])
def getNews(courseid):
    course = db.session.query(Course).filter(Course.id == courseid).first()
    posts = course.posts
    jsonStr = json.dumps([e.toJSON() for e in posts])
    return jsonify(jsonStr)


@api.route('/course/<courseid>/teacher', methods=['GET'])
def getTeachers(courseid):
    course = db.session.query(Course).filter(Course.id == courseid).first()
    teachers = course.teachers
    jsonStr = json.dumps([e.toJSON() for e in teachers])
    return jsonify(jsonStr)
