from flask import Flask
from .routes import main
import os

def create_app():
    app = Flask(__name__)
    path = os.getcwd()
    app.config['UPLOAD_FOLDER'] = 'main/static/input'

    app.secret_key = 'SECRET_KEY'
    app.register_blueprint(main)
    return app
    