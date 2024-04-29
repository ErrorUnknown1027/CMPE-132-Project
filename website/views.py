from flask import Blueprint, redirect, render_template, request, flash, jsonify, url_for
from flask_login import login_required, current_user

from .models import Book, CheckedBook, User
from . import db
import json

views = Blueprint('views', __name__)

#home page
@views.route("/")
def home():
    return render_template("home.html")

#browse book age
@views.route("/browse")
def browse():
    books = Book.query.all()
    return render_template("browse.html", books=books)

@views.route("/select_book/<int:book_id>")
@login_required
def select_book(book_id):
    book = Book.query.get_or_404(book_id)
    if CheckedBook.query.filter_by(user_id=current_user.id, book_id=book_id).first():
        flash('You already have this book selected', category='error')
    else:
        checked_book = CheckedBook(user_id=current_user.id, book_id=book_id)
        db.session.add(checked_book)
        db.session.commit()
        flash('Book selected', category='success')
    return redirect(url_for('views.browse'))

#logout page
@views.route("/logout")
def logout():
    return redirect(url_for("views.home"))

#add / remove book page
@views.route("/bookBase", methods=['GET', 'POST'])
def bookBase():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')

        book = Book.query.filter_by(title=title).first()
        if book:
            flash('Already have copy of book', category='error')
        else:
            #add book to database
            new_book = Book(title=title, authorname=author)
            db.session.add(new_book)
            db.session.commit()
            flash('Book added', category='success')
        
    books = Book.query.all()
    return render_template("bookBase.html", books=books)

#delete book
@views.route("/delete_book/<int:book_id>", methods=['GET', 'POST'])
@login_required
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    flash('Book deleted', category='success')
    return redirect(url_for('views.bookBase'))

#add / remove account page
@views.route("/userBase")
@login_required
def userBase():
    users = User.query.all()
    return render_template("userBase.html", users=users)

#delete user
@views.route("/delete_user/<int:user_id>", methods=['GET', 'POST'])
@login_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    if user.id == current_user.id:
        flash('You cannot delete yourself', category='error')
        return redirect(url_for('views.userBase'))
    db.session.delete(user)
    db.session.commit()
    flash('User deleted', category='success')
    return redirect(url_for('views.userBase'))

@views.route("/checkedBooks")
@login_required
def checkedBase():
    checked_books = CheckedBook.query.filter_by(user_id=current_user.id).all()
    return render_template("checkedBooks.html", checked_books=checked_books)


