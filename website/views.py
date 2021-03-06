from flask import render_template, request, redirect, url_for
from website import app, db, login_manager
from website.mod_news.models import Post
from website.mod_auth.models import User
import os
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from flask import send_from_directory


@app.url_defaults
def hashed_static_file(endpoint, values):
    if 'static' == endpoint or endpoint.endswith('.static'):
        filename = values.get('filename')
        if filename:
            blueprint = request.blueprint
            if '.' in endpoint:  # blueprint
                blueprint = endpoint.rsplit('.', 1)[0]

            static_folder = app.static_folder
           # use blueprint, but dont set `static_folder` option
            if blueprint and app.blueprints[blueprint].static_folder:
                static_folder = app.blueprints[blueprint].static_folder

            fp = os.path.join(static_folder, filename)
            if os.path.exists(fp):
                values['_'] = int(os.stat(fp).st_mtime)


@app.route('/')
@app.route('/index')
def index():
    posts = db.session.query(Post).limit(6).all()
    return render_template('index.html', posts=posts, pageNum=1)


@app.route('/about')
def about():
    return render_template('about.html', pageNum=6)


@app.route('/user/<userid>')
def showUser(userid):
    user = db.session.query(User).filter(User.id == userid).first()
    return render_template('personal.html', user=user, pageNum=0)


@app.route('/personal')
def personal():
    return render_template('personal.html', user=current_user, pageNum=0)


if __name__ == '__main__':
    app.run(port=8080)
