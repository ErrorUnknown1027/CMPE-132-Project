from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin): 
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    first_name = db.Column(db.String(100))
    role = db.Column(db.String(20))

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    authorname = db.Column(db.String(100))
    
class CheckedBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    timestamp = db.Column(db.DateTime, default=func.now())

    user = db.relationship('User', backref=db.backref('checked_books', lazy=True))
    book = db.relationship('Book', backref=db.backref('checked_books', lazy=True))
