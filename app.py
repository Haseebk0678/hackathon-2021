from flask import Flask, render_template
from flask import request
from model import get_state_names, get_state_index

# from .model import
app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def home():
    return render_template('index.html')


@app.route('/result', methods = ['POST','GET'])
def res():
  if request.method == 'POST':
    s = request.form['stateName']
    sn = get_state_names() # list of state names
    # if state exists
    if s in sn:
        total_first_dose = get_state_index(s,sn)[-2]
        total_second_dose = get_state_index(s,sn)[-1]

    return render_template('result.html',s = s, total_second_dose=total_second_dose, total_first_dose=total_first_dose)

if __name__ == '__main__':
    app.run(debug=True)
