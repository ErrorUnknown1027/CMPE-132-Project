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
    return render_template("browse.html")

#logout page
@views.route("/logout")
def logout():
    return redirect(url_for("views.home"))

#checkout book page
@views.route("/checkout")
def checkout():
    return render_template("checkout.html")

#add / remove book page
@views.route("/bookBase")
def bookBase():
    return render_template("bookBase.html")

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
