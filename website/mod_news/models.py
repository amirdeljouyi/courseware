from website import db

tags_posts = db.Table('tags-posts',
                             db.Column('tag_id', db.Integer, db.ForeignKey(
                                 'tag.id'), primary_key=True),
                             db.Column('post_id', db.Integer,
                                       db.ForeignKey('post.id'), primary_key=True))
class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    posts = db.relationship('Post', backref='category', lazy='dynamic')

class Slider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    tags = db.relationship('Tag',
                                  secondary=tags_posts, backref='posts', lazy='dynamic')
    title = db.Column(db.String(120), nullable=True)
    img_url = db.Column(db.String(120), nullable=True)
    content_mini = db.Column(db.String(180), nullable=True)
    content = db.Column(db.Text, nullable=True)
    date = db.Column(db.String(120), nullable=True)
    
    def toJSON(self):
        return {
            'id':self.id,
            'title': self.title,
            'img_url':self.img_url,
            'content':self.content,
            'content_mini':self.content_mini,
            'date':self.date,
        }

    def __str__(self):
        return str(self.id) + ' ' + str(self.title)