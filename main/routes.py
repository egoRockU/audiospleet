from flask import Blueprint, render_template, request, session, jsonify
import time

main = Blueprint('main', __name__)

@main.route('/hellos')
def hello():
    return 'Hello, World!'

@main.route('/')
def home():
    session['file_valid'] = False  
    return render_template("home.html")

@main.route('/checkfile', methods=['POST'])
def checkfile():
    types = ['mp3', 'wav', 'flac', 'm4a']

    try:
        audio = request.files['audio']
    except Exception as err:
         print("Error" + repr(err))
         return render_template('validate_results/nofile.html')
    
    audio_ext = audio.filename.split('.')[-1]
    for audio_type in types:
        if audio_ext == audio_type:
            session['file_valid'] = True
            return render_template('validate_results/valid.html')
    return render_template('validate_results/invalid.html')


@main.route('/spleet', methods=['POST'])
def spleet():
    print('reached here')
    return "Hello"