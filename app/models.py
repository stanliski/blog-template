# -*- coding: utf-8 -*-

from app import db
from datetime import datetime


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    email = db.Column(db.String(20))
    register_time = db.Column(db.DateTime)
    confirmed = db.Column(db.Boolean, default=False)

    blogs = db.relationship('Blog', backref='user', lazy='dynamic')
    comments = db.relationship('Comment', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % self.username


class Topic(db.Model):

    __tablename__ = 'topics'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unqiue=True)
    create_time = db.Column(db.DateTime)

    blogs = db.relationship('Blog', backref='topic', lazy='dynamic')

    def __repr__(self):
        return '<Topic %r>' % self.title

    def __init__(self, **kwargs):
        super(Topic, self).__init__(**kwargs)


class Keywords(db.Model):

    __tablename__ = 'keywords'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True)
    create_time = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return '<Keywords %r>' % self.title

    def __init__(self, **kwargs):
        super(Keywords, self).__init__(**kwargs)



class Blog(db.Model):

    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True)
    brief = db.Column(db.String(200))
    content = db.Column(db.Text)
    create_time = db.Column(db.DateTime, default=datetime.now())
    update_time = db.Column(db.DateTime)
    status = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'))


    def __repr__(self):
        return '<Blog %r>' % self.title

    def __init__(self, **kwargs):
        super(Blog, self).__init__(**kwargs)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def to_json(self):
        json = dict(title=self.title, content=self.content,
                         status=self.status, update_time=self.update_time, create_time=self.create_time)
        return json



class Comment(db.Model):

    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100))
    create_time = db.Column(db.DateTime, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Comment %r>' % self.content

    def __init__(self, **kwargs):
        super(Comment, self).__init__(**kwargs)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def to_json(self):
        json = dict(content=self.content, create_time=self.create_time)