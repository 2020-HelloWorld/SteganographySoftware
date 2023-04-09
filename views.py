from flask import Blueprint, render_template, request, flash, redirect, url_for, send_from_directory, current_app
import os
views = Blueprint('views', __name__)


#MULTIPLE ROUTES FROM SAME PAGE : https://stackoverflow.com/questions/18290142/multiple-forms-in-a-single-page-using-flask-and-wtforms
#FILE HANDLING : https://stackoverflow.com/questions/46136478/flask-upload-how-to-get-file-name#:~:text=Once%20you%20fetch%20the%20actual,filename%20.
#DOWNLOAD FILE : https://stackoverflow.com/questions/24577349/flask-download-a-file
#PASS ARG TO REDIRECT : https://stackoverflow.com/questions/17057191/redirect-while-passing-arguments
#FORM FILE UPLOAD : https://www.w3schools.com/tags/att_form_enctype.asp
#CURRENT APP : https://www.fullstackpython.com/flask-globals-current-app-examples.html
#FULL PATH : https://www.geeksforgeeks.org/python-os-path-join-method/

import InAny    #embed #extract
import InAudio  #embed #extract
import InImage  #encode #decode
import Client_Thread
import Server_Thread


#FUNTIONAL ROUTES 

#TEXT TO IMG
@views.route('/imageencode', methods=['GET', 'POST'])
def imageencode():
    #file-encode
    #secret-key-encode
    if request.method == 'POST':
        uploads = os.path.join(current_app.root_path, current_app.config['UPLOAD_FOLDER'])
        
        message = request.form.get("secret-key-encode")
        file = request.files['file-encode']
        if file.filename!="":
            file.save(os.path.join(uploads,file.filename))
        
        host = file.filename
        result = list(host.split("."))
        result[-2] += "(new)"
        result = ".".join(result)
        InImage.encode(os.path.join(uploads,file.filename),message,os.path.join(uploads,result))
        return send_from_directory(uploads,result,as_attachment=True)
    return redirect(url_for('views.dashboard'))

@views.route('/imagedecode', methods=['GET', 'POST'])
def imagedecode():
    #file-decode
    if request.method=="POST":
        uploads = os.path.join(current_app.root_path, current_app.config['UPLOAD_FOLDER'])
        file = request.files['file-decode']
        if file.filename!="":
            file.save(os.path.join(uploads,file.filename))
        
        data = InImage.decode(os.path.join(uploads,file.filename))
        print(data)
    return redirect(url_for('views.endpage',data=data)) 

#TEXT TO AUDIO
@views.route('/audioencode', methods=['GET', 'POST'])
def audioencode():
    #file-encode
    #secret-key-encode
    if request.method == 'POST':
        uploads = os.path.join(current_app.root_path, current_app.config['UPLOAD_FOLDER'])
        
        message = request.form.get("secret-key-encode")
        file = request.files['file-encode']
        if file.filename!="":
            file.save(os.path.join(uploads,file.filename))
        
        host = file.filename
        result = list(host.split("."))
        result[-2] += "(new)"
        result = ".".join(result)
        InAudio.embed(os.path.join(uploads,file.filename),message,os.path.join(uploads,result))
        return send_from_directory(uploads,result,as_attachment=True)
    return redirect(url_for('views.dashboard')) 

@views.route('/audiodecode', methods=['GET', 'POST'])
def audiodecode():
    #file-decode
    if request.method=="POST":
        uploads = os.path.join(current_app.root_path, current_app.config['UPLOAD_FOLDER'])
        file = request.files['file-decode']
        if file.filename!="":
            file.save(os.path.join(uploads,file.filename))
        
        data = InAudio.extract(os.path.join(uploads,file.filename))
        print(data)
    return redirect(url_for('views.endpage',data=data)) 

#ANY TO ANY
@views.route('/anyencode', methods=['GET', 'POST'])
def anyencode():
    if request.method == 'POST':
        uploads = os.path.join(current_app.root_path, current_app.config['UPLOAD_FOLDER'])
        
        message = request.form.get("secret-data-encode")
        print(message)
        file = request.files['file-encode']
        if file.filename!="":
            file.save(os.path.join(uploads,file.filename))
        print(message)
        host = file.filename
        result = list(host.split("."))
        result[-2] += "_new"
        result = ".".join(result)
        print(result)
        InAny.embed(os.path.join(uploads,file.filename),message,os.path.join(uploads,result))
        return send_from_directory(uploads,result,as_attachment=True)
    return redirect(url_for('views.dashboard')) 

@views.route('/anydecode', methods=['GET', 'POST'])
def anydecode():
    #file-decode
    #output-format
    if request.method == 'POST':
        uploads = os.path.join(current_app.root_path, current_app.config['UPLOAD_FOLDER'])
        type = request.form.get("output-format")
        file = request.files['file-decode']
        if file.filename!="":
            file.save(os.path.join(uploads,file.filename))
        
        host = list(file.filename.split("."))
        host[-1] = type
        host = ".".join(host)
        InAny.extract(os.path.join(uploads,file.filename),type)
        return send_from_directory(uploads,host,as_attachment=True)
    return redirect(url_for('views.dashboard')) 

#COVERT BURST
@views.route('/sendburst', methods=['GET', 'POST'])
def sendburst():
    #receiver-ip
    #host-file
    #secret-data
    if request.method == 'POST':
        message = request.form.get("secret-data")
        ip = request.form.get("receiver-ip")
        print(ip,message)
        # try:
        Client_Thread.burstclient(ip,message)
        # except Exception as e: 
        #     print("SERVER DOWN",e)

    return redirect(url_for('views.dashboard')) 

@views.route('/receiveburst', methods=['GET', 'POST'])
def receiveburst():
    
    uploads = os.path.join(current_app.root_path, current_app.config['UPLOAD_FOLDER'])
    try:
        file = Server_Thread.burstserver()
        return send_from_directory(uploads,file,as_attachment=True)
    except:
        print("DATA CORRUPTED IN TRANSIT")
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

#--- OUTPUT
@views.route('/endpage/<data>', methods=['GET', 'POST'])
def endpage(data):
    return render_template("output.html",secret_output=data)

@views.route('/endpage/backhome', methods=['GET', 'POST'])
def backhome():
    return redirect(url_for('views.dashboard')) 