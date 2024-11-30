from utils.db import db


# parent table

class Personal(db.Model):
    personName = db.Column(db.String(100), primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(100), nullable=False)
    birthdate = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    firstname = db.Column(db.String(100), nullable=False)
    birthYear = db.Column(db.String(100), nullable=False)
    birthMonth = db.Column(db.String(100), nullable=False)
    birthDay= db.Column(db.String(100), nullable=False)
    city= db.Column(db.String(100), nullable=False)
    rank = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)


class Business(db.Model):
    rank = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(100), nullable=False)
    finalWorth = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    organization = db.Column(db.String(100), nullable=False)
    selfMade = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(100), nullable=False)
    industries= db.Column(db.String(100), nullable=False)
    title= db.Column(db.String(100), nullable=False)
    state= db.Column(db.String(100), nullable=False)




class Country(db.Model):
    country = db.Column(db.String(100),  primary_key=True)
    countryOfCitizenship = db.Column(db.String(100), nullable=False)
    cpi_country = db.Column(db.String(100), nullable=False)
    cpi_change_country = db.Column(db.String(100), nullable=False)
    gdp_country = db.Column(db.String(100), nullable=False)
    gross_tertiary_education_enrollment=db.Column(db.String(100), nullable=False)
    life_expectancy_country=db.Column(db.String(100), nullable=False)
    tax_revenue_country_country=db.Column(db.String(100), nullable=False)
    gross_primary_education_enrollment_country=db.Column(db.String(100), nullable=False)
    total_tax_rate_country=db.Column(db.String(100), nullable=False)
    latitude_country = db.Column(db.String(100), nullable=False)
    longitude_country = db.Column(db.String(100), nullable=False)
    residenceStateRegion= db.Column(db.String(100), nullable=False)
    population_country= db.Column(db.String(100), nullable=False)
    rank = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)





