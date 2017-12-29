from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)  # global flask object

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql+pymysql://root:root@localhost:3306/db'

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = 'auth.login' 
login_manager.init_app(app)

from website.mod_auth.views import mod_auth as auth_module
from website.mod_news.views import mod_news as news_module
from website.mod_course.views import mod_course as course_module

# Register blueprint(s)
app.register_blueprint(auth_module)
app.register_blueprint(news_module)
app.register_blueprint(course_module)

from website import models
from website.mod_auth.models import User

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)

from website import views
