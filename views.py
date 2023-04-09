from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify

views = Blueprint('views', __name__)

#FUNTIONAL ROUTES 
#MULTIPLE ROUTES FROM SAME PAGE : https://stackoverflow.com/questions/18290142/multiple-forms-in-a-single-page-using-flask-and-wtforms
#FILE HANDLING : https://stackoverflow.com/questions/46136478/flask-upload-how-to-get-file-name#:~:text=Once%20you%20fetch%20the%20actual,filename%20.

#TEXT TO IMG
@views.route('/imageencode', methods=['GET', 'POST'])
def imageencode():
    #file-encode
    #secret-key-encode
    return redirect(url_for('views.dashboard'))

@views.route('/imagedecode', methods=['GET', 'POST'])
def imagedecode():
    #file-decode
    return redirect(url_for('views.dashboard')) 

#TEXT TO AUDIO
@views.route('/audioencode', methods=['GET', 'POST'])
def audioencode():
    #file-encode
    #secret-key-encode
    return redirect(url_for('views.dashboard')) 

@views.route('/audiodecode', methods=['GET', 'POST'])
def audiodecode():
    #file-decode
    return redirect(url_for('views.dashboard')) 

#ANY TO ANY
@views.route('/anyencode', methods=['GET', 'POST'])
def anyencode():
    #file-encode
    #secret-data-encode
    return redirect(url_for('views.dashboard')) 

@views.route('/anydecode', methods=['GET', 'POST'])
def anydecode():
    #file-decode
    #output-format
    return redirect(url_for('views.dashboard')) 

#COVERT BURST
@views.route('/sendburst', methods=['GET', 'POST'])
def sendburst():
    #receiver-ip
    #host-file
    #secret-data
    return redirect(url_for('views.dashboard')) 

@views.route('/receiveburst', methods=['GET', 'POST'])
def receiveburst():
    return redirect(url_for('views.dashboard')) 

#COVERT TIMESTAMP
@views.route('/sendtimestamp', methods=['GET', 'POST'])
def sendtimestamp():
    #receiver-ip
    #host-file
    #secret-data
    return redirect(url_for('views.dashboard'))

@views.route('/receivetimestamp', methods=['GET', 'POST'])
def receivetimestamp():
    return redirect(url_for('views.dashboard'))


#------------------------------------------------------------------------------------#


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