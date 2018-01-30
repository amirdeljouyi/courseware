from website import db

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.relationship('User', backref='professor',
                           uselist=False)
    field_of_study = db.Column(db.String(100), nullable=True)
    degree = db.Column(db.String(30), nullable=True)
    level = db.Column(db.String(30), nullable=True)

    def toJSON(self):
        return {
            'id':self.user.id,
            'firstname': self.user.first_name,
            'lastname': self.user.last_name,
            'img_url':self.user.img_url,
            'field_of_study':self.field_of_study,
            'degree':self.degree,
            'level':self.level,
        }