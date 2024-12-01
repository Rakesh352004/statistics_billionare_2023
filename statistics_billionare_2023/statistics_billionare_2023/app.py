from flask import Flask, render_template, request, redirect
from utils.db import db
from models.data import *
from flask_sqlalchemy import SQLAlchemy


flask_app = Flask(__name__)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'




@flask_app.route('/')
def index():
    data = Business.query.all()
    return render_template('index.html', content=data)


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


with flask_app.app_context():
    db.create_all()



@flask_app.route('/submit', methods=['POST'])
def submit():
    form_data = request.form.to_dict()
    print(f"form_data: {form_data}")

    personName = form_data.get('personName')
    age = form_data.get('age')
    gender = form_data.get('gender')
    birthdate = form_data.get('birthdate')
    city = form_data.get('city')
    state = form_data.get('state')
    country = form_data.get('country')




    rank = form_data.get('rank')
    source = form_data.get('source')
    finalWorth = form_data.get('finalWorth')
    category = form_data.get('category')
    organization = form_data.get('organization')
    industries = form_data.get('industries')
    title = form_data.get('title')

    person = Person.query.filter_by(personName=personName).first()
    if not person:
        author = Person(personName=personName, age=age, gender=gender,birthdate=birthdate, city=city,state=state,country=country)
        db.session.add(person)
        db.session.commit()

    data = Business(rank=rank, source=source, finalWorth=finalWorth, category=category,organization=organization, industries=industries, title=title,person_id=person.id)
    db.session.add(data)
    db.session.commit()
    print("sumitted successfully")
    return redirect('/')


if __name__ == '__main__':
    flask_app.run(
        host='127.0.0.1',
        port=8005,
        debug=True
    )