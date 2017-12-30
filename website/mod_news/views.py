from flask import Blueprint, render_template, request, redirect, url_for
from website import app, db
from website.mod_news.models import Post, Category, Tag
from time import gmtime, strftime
from flask_login import login_required, current_user

# Define the blueprint: 'news', set its url prefix: app.url/news
mod_news = Blueprint('news', __name__, url_prefix='/news')


@mod_news.route('/add', methods=['GET', 'POST'])
@login_required
def addNews():
    if request.method == "POST":
        if request.form['content'] == '' or request.form['content'] == None:
            print('Not exists')
        else:
            p = Post(
                title=request.form['title'],
                user=current_user,
                content=request.form['content'],
                date=strftime("%Y-%m-%d %H:%M:%S", gmtime()),
                img_url=request.form['img_url'],
                category=setCategory(request.form['category']),
            )
            p.tags.extend(setTags(request.form.getlist('tags')))

            db.session.add(p)
            db.session.commit()
            result = request.form['content']

        for a in request.form.keys():
            print(a, request.form[a])
    return render_template('news/add.html')


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
def news():
    posts = db.session.query(Post).all()
    categories = db.session.query(Category).all()
    return render_template('news/list.html', posts=posts, tagsOrCategories=categories, tag=False, pageName="all", pageNum=2)


@mod_news.route('/category/<categoryid>')
def showCategory(categoryid):
    category = db.session.query(Category).filter(
        Category.id == categoryid).first()
    posts = category.posts
    pageName = category.name
    categories = db.session.query(Category).all()
    return render_template('news/list.html', posts=posts, tagsOrCategories=categories, tag=False, pageName=pageName, pageNum=2)


@mod_news.route('/tags/<tagid>')
def showTag(tagid):
    tag = db.session.query(Tag).filter(
        Tag.id == tagid).first()
    posts = tag.posts
    pageName = tag.name
    tags = db.session.query(Tag).all()
    return render_template('news/list.html', posts=posts, tagsOrCategories=tags, tag=True, pageName=pageName, pageNum=2)


@mod_news.route('/<postid>')
def showPost(postid):
    post = db.session.query(Post).filter(Post.id == postid).first()
    return render_template('news/detail.html', post=post, pageNum=2)
