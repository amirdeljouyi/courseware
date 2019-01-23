from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager
from werkzeug.utils import secure_filename

#--------------- PAGINATION ---------------
POSTS_PER_PAGE = 6


#--------------- UPLOADING ----------------
UPLOAD_FOLDER = '/run/media/amirdeljuyi/B6A4E8E5A4E8A8D7/Developing/Programming/Web Based/Internet Engineering/Internet Engineering-9312268118/website/static'
IMG_FOLDER = '/img'
VIDEO_FOLDER = '/video'
HOMEWORK_FOLDER = '/homework'
ALLOWED_EXTENSIONS = set(
    ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'webm', 'mp4', 'pdf'])


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


app = Flask(__name__)  # global flask object

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql+pymysql://root:root@localhost:3306/db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['IMG_FOLDER'] = UPLOAD_FOLDER + IMG_FOLDER
app.config['VIDEO_FOLDER'] = UPLOAD_FOLDER + VIDEO_FOLDER
app.config['HOMEWORK_FOLDER'] = UPLOAD_FOLDER + HOMEWORK_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['POSTS_PER_PAGE'] = POSTS_PER_PAGE
app.debug = True

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from website.mod_auth.views import mod_auth as auth_module
from website.mod_news.views import mod_news as news_module
from website.mod_professor.views import mod_professor as professor_module
from website.mod_student.views import mod_student as student_module
from website.mod_course.views import mod_course as course_module
from website.api.api import api as api


# Register blueprint(s)
app.register_blueprint(auth_module)
app.register_blueprint(news_module)
app.register_blueprint(professor_module)
app.register_blueprint(student_module)
app.register_blueprint(course_module)
app.register_blueprint(api)

from website.mod_auth.models import User


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)


from website import views
