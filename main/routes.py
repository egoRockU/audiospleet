from flask import Blueprint, render_template, request, session, send_file, Response, url_for, current_app
from werkzeug.utils import secure_filename
import time, os

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
    audio = request.files['audio']
    stem = request.form['stem']
    filename = secure_filename(audio.filename)
    path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    print(path)
    audio.save(path)

    response = Response()
    response.headers['HX-Redirect'] = url_for('main.download', filename=filename)

    return response


@main.route('/download/<filename>')
def download(filename):
   return send_file(f"static/input/{filename}", download_name=filename, as_attachment=True) 