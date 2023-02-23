from flask import Flask,render_template,request,redirect,url_for,flash,session,jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    jpg_files = os.listdir('static/assets/qs') 
    index_count = len(jpg_files)   
    return render_template('index.html', index_count=index_count)

@app.route('/sketch_all')
def sketch_all():
    return render_template('sketch_string.html')

@app.route('/sketch_gd')
def sketch_gd():
    return render_template('sketch_gd2.html')

@app.route('/sketch_pix')
def sketch_pix():
    return render_template('sketch_pix.html')

@app.route('/sketch<index>')
def sketch(index):
    index = int(index) + 1
    index_name = "%03d"%int(index) 
    return render_template('sketch_two.html',index_name = index_name)

@app.route('/sketch_no<index>')
def sketch_no(index):
    index_name = "%03d"%int(index)
    return render_template('sketch_NoBG.html',index_name = index_name)

@app.route('/wave<index>')
def wave(index):
    index_name = "%03d"%int(index)
    return render_template('wave.html',index_name = index_name)
