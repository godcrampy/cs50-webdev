from flask import Flask, render_template, request, session
from flask_session import Session
import datetime

app = Flask(__name__)
notes = []

app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


@app.route('/')
def index():
    headline = 'Hellah'
    return render_template('index.html', headline=headline)

@app.route('/hello', methods = ['POST', 'GET'])
def hello():
    if request.method == 'GET':
        return render_template('hello.html', name="")
    name = request.form.get('name')
    return render_template('hello.html', name=name)

@app.route('/newyear')
def new_year():
    now = datetime.datetime.now()
    is_new_year = now.month == 1 and now.day == 1
    return render_template('new_year.html', is_new_year=is_new_year)

@app.route('/names')
def names():
    names = ['steve', 'bill', 'burlsmith']
    return render_template('names.html', names=names)

@app.route('/fruits')
def fruits():
    fruits = ['apple', 'banana', 'orange', 'cherries']
    return render_template('fruits.html', fruits=fruits)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/notes', methods=['GET', 'POST'])
def todo():
    if session.get('notes') is None:
        session['notes'] = []
    if request.method == 'POST':
        note = request.form.get('note')
        session['notes'].append(note)

    return render_template('notes.html', notes=session['notes'])
    