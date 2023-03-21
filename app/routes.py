from app import app
from flask import render_template

@app.route('/')
def hello_world():
    return render_template('base.html', name = "Aaron")

@app.route('/test')
def hello_test():
    return render_template('test.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

