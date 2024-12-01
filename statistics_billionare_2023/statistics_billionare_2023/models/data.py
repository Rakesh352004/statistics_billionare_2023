from utils.db import db


# parent table

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    personName = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(100), nullable=False)
    birthdate = db.Column(db.String(100), nullable=False)
    city= db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)

    data = db.relationship('Business', backref='person', lazy=True)




class Business(db.Model):
    business_id = db.Column(db.Integer, primary_key=True)
    rank = db.Column(db.Integer, nullable=False)
    source = db.Column(db.String(100), nullable=False)
    finalWorth = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    organization = db.Column(db.String(100), nullable=False)
    industries= db.Column(db.String(100), nullable=False)
    title= db.Column(db.String(100), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)











