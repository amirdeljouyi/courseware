from flask import Blueprint, render_template, request, redirect, url_for
from website import app, db, allowed_file
from website.mod_news.models import Post, Category, Tag
from time import gmtime, strftime
from flask_login import current_user
from website.mod_auth.views import login_required
from werkzeug.utils import secure_filename
import os

# Define the blueprint: 'news', set its url prefix: app.url/news
mod_news = Blueprint('news', __name__, url_prefix='/news')


@mod_news.route('/add', methods=['GET', 'POST'])
@login_required(role='Admin')
def addNews():
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
                category=setCategory(request.form['category']),
            )
            p.tags.extend(setTags(request.form.getlist('tags')))

            db.session.add(p)
            db.session.commit()
            result = request.form['content']

    return render_template('news/add&edit.html')


@mod_news.route('/edit/<newsid>', methods=['GET', 'POST'])
@login_required(role="Admin")
def editNews(newsid):
    p = db.session.query(Post).filter(Post.id == newsid).first()
    if request.method == "POST":
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['IMG_FOLDER'], filename))
            p.img_url=filename
        p.title=request.form['title'],
        p.content=request.form['content'],
        p.date=strftime("%Y-%m-%d %H:%M:%S", gmtime()),
        #p.category=setCategory(request.form['category']),
        db.session.commit()
    return render_template('news/add&edit.html', news=p)


@mod_news.route('/delete/<postid>', methods=['POST'])
@login_required(role="Admin")
def deleteNews(postid):
    p = db.session.query(Post).filter(Post.id == postid).first()
    db.session.delete(p)
    db.session.commit()
    posts = db.session.query(Post).paginate(
        1, app.config['POSTS_PER_PAGE'], False)
    categories = db.session.query(Category).all()
    return render_template('news/list.html',tc=False, posts=posts, tagsOrCategories=categories, tag=False, pageName="all", pageNum=2)


def setCategory(category):
    categories = \
        [db.session.query(Category).filter(
            Category.name == "it").first(), db.session.query(Category).filter(
            Category.name == "sport").first(), db.session.query(Category).filter(
            Category.name == "science").first(), db.session.query(Category).filter(
            Category.name == "culture").first(), db.session.query(Category).filter(
            Category.name == "course").first()]
    for cat in categories:
        if(category == cat.name):
            return cat


def setTags(tags):
    tagsDB = \
        [db.session.query(Tag).filter(
            Tag.name == "ai").first(), db.session.query(Tag).filter(
            Tag.name == "event").first(), db.session.query(Tag).filter(
            Tag.name == "health").first(), db.session.query(Tag).filter(
            Tag.name == "museum").first(), db.session.query(Tag).filter(
            Tag.name == "tour").first(), db.session.query(Tag).filter(
            Tag.name == "exam").first()]
    retTags = []
    for tag in tags:
        for tagDB in tagsDB:
            if(tag == tagDB.name):
                retTags.append(tagDB)
    return retTags


@mod_news.route('/')
@app.route('/page/<int:page>')
def news(page=1):
    posts = db.session.query(Post).paginate(
        page, app.config['POSTS_PER_PAGE'], False)
    categories = db.session.query(Category).all()
    return render_template('news/list.html', posts=posts,tc=False, tagsOrCategories=categories, tag=False, pageName="all", pageNum=2)


@mod_news.route('/category/<categoryid>')
def showCategory(categoryid):
    category = db.session.query(Category).filter(
        Category.id == categoryid).first()
    posts = category.posts
    pageName = category.name
    categories = db.session.query(Category).all()
    return render_template('news/list.html', posts=posts,tc=True, tagsOrCategories=categories, tag=False, pageName=pageName, pageNum=2)


@mod_news.route('/tags/<tagid>')
def showTag(tagid):
    tag = db.session.query(Tag).filter(
        Tag.id == tagid).first()
    posts = tag.posts
    pageName = tag.name
    tags = db.session.query(Tag).all()
    return render_template('news/list.html', posts=posts,tc=True, tagsOrCategories=tags, tag=True, pageName=pageName, pageNum=2)


@mod_news.route('/<postid>')
def showPost(postid):
    post = db.session.query(Post).filter(Post.id == postid).first()
    return render_template('news/detail.html', post=post, pageNum=2)
