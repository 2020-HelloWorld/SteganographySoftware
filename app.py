from flask import Flask
from os import path

def create_app():
    
    app = Flask(__name__)
    UPLOAD_FOLDER = 'uploads'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'

    from views import views
    app.register_blueprint(views, url_prefix='/')

    return app

