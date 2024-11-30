from flask import Flask, render_template, request, redirect
from utils.db import db
from models.data import *


flask_app = Flask(__name__)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'



@flask_app.route('/')
def index():
    return render_template('index.html')


@flask_app.route('/help')
def help():
    return render_template('help.html')


@flask_app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@flask_app.route('/add_data')
def add_data():
    return render_template('add_data.html')

db.init_app(flask_app)









if __name__ == '__main__':
    flask_app.run(
        host='127.0.0.1',
        port=8005,
        debug=True
    )