from flask import Flask,render_template,request,redirect,url_for,flash,session,jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    jpg_files = os.listdir('static/assets') 
    index_count = len(jpg_files)   
    return render_template('index.html', index_count=index_count)


@app.route('/sketch<index>')
def sketch(index):
    index_name = "%02d"%int(index)
    return render_template('sketch_loop.html',index_name = index_name)

@app.route('/sketch_no<index>')
def sketch_no(index):
    index_name = "%02d"%int(index)
    return render_template('sketch_NoBG.html',index_name = index_name)

@app.route('/wave<index>')
def wave(index):
    index_name = "%02d"%int(index)
    return render_template('wave.html',index_name = index_name)
