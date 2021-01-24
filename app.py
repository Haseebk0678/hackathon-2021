from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

print("hellos")
@app.route("/", methods = ['POST', 'GET'])
def home():
    return render_template('index.html')
    if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)




