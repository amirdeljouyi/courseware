from website import db

class Category(db.Model):
    name = db.Column(db.String(120), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    posts = db.relationship('Post', backref='category', lazy='dynamic')

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    title = db.Column(db.String(120), nullable=True)
    img_url = db.Column(db.String(120), nullable=True)
    content_mini = db.Column(db.String(180), nullable=True)
    content = db.Column(db.Text, nullable=True)
    date = db.Column(db.String(120), nullable=True)
    tags = db.Column(db.String(120), nullable=True)

    def __str__(self):
        return str(self.id) + ' ' + str(self.title)