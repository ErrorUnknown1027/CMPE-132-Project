from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin): 
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    first_name = db.Column(db.String(100))
    
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    authorname = db.Column(db.String(100))
    
class Checkout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)

    user = db.relationship('User', backref='checkouts')
    book = db.relationship('Book', backref='checkouts')