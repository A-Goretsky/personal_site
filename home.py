from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/programmming')
def program_page():
    return render_template('program.html')

@app.route('/photography')
def photo_page():
    return render_template('photo.html')

@app.route('/videography')
def video_page():
    return render_template('video.html')
