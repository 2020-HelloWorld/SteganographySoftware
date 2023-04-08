from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify

views = Blueprint('views', __name__)

#FUNTIONAL ROUTES






























# NON-FUNTIONAL ROUTES

@views.route('/', methods=['GET', 'POST'])
def landing():
    return render_template("landing.html")

@views.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template("dashboard.html")

#--- DASHBOARD ROUTES

@views.route('/covert', methods=['GET', 'POST'])
def covertdash():
    return render_template("covertlist.html")

@views.route('/local', methods=['GET', 'POST'])
def localdash():
    return render_template("locallist.html")

#--- COVERT ROUTES

@views.route('/burst', methods=['GET', 'POST'])
def burst():
    return render_template("covert-burst.html")

@views.route('/timestamp', methods=['GET', 'POST'])
def timestamp():
    return render_template("covert-timestamp.html")

#--- LOCAL ROUTES

@views.route('/anytoany', methods=['GET', 'POST'])
def anytoany():
    return render_template("any-file.html")

@views.route('/texttoimg', methods=['GET', 'POST'])
def texttoimg():
    return render_template("text-to-image.html")

@views.route('/texttoaudio', methods=['GET', 'POST'])
def texttoaudio():
    return render_template("text-to-audio.html")