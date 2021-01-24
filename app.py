from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def home():
    return render_template('index.html')

    
@app.route("/result", methods = ['POST','GET'])
def res():
  if request.method == 'POST':
    s = request.form['stateName']
    return render_template("result.html",s = s)



