from flask import Flask, render_template,request, redirect, session
from flask_mysqldb import MySQL
import yaml
import os
import numpy as np
import pandas as pd
from knn import knn
from flask_uploads import UploadSet , configure_uploads , IMAGES 

UPLOAD_FOLDER = 'static/uploadedimages'


app = Flask(__name__)

# photos = UploadSet('photos', IMAGES)

# app.config['UPLOADED_PHOTOS_DEST'] = UPLOAD_FOLDER
# configure_uploads(app,photos)
# app.secret_key = os.urandom(24)

# # configure databasesi
# db = yaml.load(open('db.yaml'))
# app.config['MYSQL_HOST'] = db['mysql_host']
# app.config['MYSQL_USER'] = db['mysql_user']
# app.config['MYSQL_PASSWORD'] = db['mysql_password']
# app.config['MYSQL_DB'] = db['mysql_db']

# mysql = MySQL(app)

data = pd.read_csv("movies_data.csv").values
data = data[:,1:]

def find_neighbours(movie_id):
	movie = data[movie_id]
	movie  = movie[1:]
	ans = knn(data.tolist(),6,movie)
	return ans[1:]


@app.route('/',methods=['GET','POST'])

def index():
    print(str(len(data)))
    return render_template("index.html",data = data, l =len(data))

@app.route('/movie/<movie_id>',methods=['GET','POST'])
def movie(movie_id):
   rec = find_neighbours(int(movie_id))
   return render_template("movie.html",data = data[int(movie_id)], rec = rec, l = len(rec))
if __name__ == '__main__':
    app.run(debug=True)