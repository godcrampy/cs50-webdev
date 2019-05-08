from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    headline = 'Hellah'
    return render_template('index.html', headline=headline)

@app.route('/<string:name>')
def name(name):
    return f'<h1>Hello, {name}!</h1>'

@app.route('/bye')
def bye():
    headline = 'Goodbye'
    return render_template('index.html', headline=headline)

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
