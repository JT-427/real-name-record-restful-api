from . import db

class People(db.Model):
    people_id = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    gender = db.Column(db.Integer, nullable=False)
    contact_number = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(100), nullable=False)

    trace = db.relationship('Trace', backref='people', lazy='select')

class Place(db.Model):
    place_id = db.Column(db.String(48), primary_key=True)
    place_name = db.Column(db.String(45), nullable=False)
    address = db.Column(db.String(100), nullable=False)

    trace = db.relationship('Trace', backref='place', lazy='select')

class Trace(db.Model):
    people_id = db.Column(db.String(32), db.ForeignKey('people.people_id'), primary_key=True)
    place_id = db.Column(db.String(48), db.ForeignKey('place.place_id'), primary_key=True)
    time = db.Column(db.DateTime, primary_key=True, nullable=False)