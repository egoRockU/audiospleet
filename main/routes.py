from flask import Blueprint, render_template, request, session
import time

main = Blueprint('main', __name__)

@main.route('/hellos')
def hello():
    return 'Hello, World!'

@main.route('/')
def home():
    session['button_disabled'] = True  
    return render_template("home.html", button_disabled=session['button_disabled'])

@main.route('/checkfile', methods=['POST'])
def checkfile():
    types = ['mp3', 'wav', 'flac', 'm4a']
    audio = request.files['audio']
    audio_ext = audio.filename.split('.')[-1]

    for audio_type in types:
        if audio_ext == audio_type:
            session['button_disabled'] = False
            return render_template('validate_results/valid.html')
    return render_template('validate_results/invalid.html')