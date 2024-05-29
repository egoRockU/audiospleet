from flask import Blueprint, render_template, request, session, jsonify
import time

main = Blueprint('main', __name__)

@main.route('/hellos')
def hello():
    return 'Hello, World!'

@main.route('/')
def home():
    session['file_valid'] = False  
    return render_template("home.html", file_valid=False)

@main.route('/checkfile', methods=['POST'])
def checkfile():
    types = ['mp3', 'wav', 'flac', 'm4a']
    audio = request.files['audio']
    audio_ext = audio.filename.split('.')[-1]

    for audio_type in types:
        if audio_ext == audio_type:
            session['file_valid'] = True
            return render_template('validate_results/valid.html', file_valid=True)
    return render_template('validate_results/invalid.html', file_valid=False)

@main.route('/spleet', methods=['POST'])
def spleet():
    print('reached here')
    return "Hello"