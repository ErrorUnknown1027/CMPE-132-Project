from flask import Blueprint, redirect, render_template, request, flash, jsonify, url_for
from flask_login import login_required, current_user

from .models import Book
from . import db
import json

views = Blueprint('views', __name__)

#home page
@views.route("/")
def home():
    return render_template("home.html")

#browse pbook age
@views.route("/browse")
def browse():
    books = Book.query.all()
    return render_template("browse.html", books=books)

#logout page
@views.route("/logout")
def logout():
    return redirect(url_for("views.home"))

#checkout book page
@views.route("/checkout")
def checkout():
    return render_template("checkout.html")

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
def userBase():
    return render_template("userBase.html")

#checked out books page
@views.route("/checkedBooks")
def checkedBase():
    args = request.args
    name = args.get('name')
    return render_template("checkedBooks.html", name=name)
