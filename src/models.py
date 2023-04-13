from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    name = db.Column(db.String(120), unique=False, nullable=False)
    favorite_people = db.relationship('FavoritePeople', backref = 'user', lazy=True)
    favorite_planets = db.relationship('FavoritePlanets', backref= 'user', lazy=True)
    favorite_vehicles = db.relationship('FavoriteVehicles', backref= 'user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    birthdate = db.Column(db.String(80), unique=False, nullable=False)
    eyes = db.Column(db.String(80), unique=False, nullable=False)
    height = db.Column(db.Float, unique=False, nullable=False)
    favorite_people = db.relationship('FavoritePeople', backref= 'people', lazy=True)

    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birthdate": self.birthdate,
            "eyes": self.eyes,
            "height": self.height
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    population = db.Column(db.String(80), unique=False, nullable=False)
    surface = db.Column(db.String(80), unique=False, nullable=False)
    diameter = db.Column(db.String(80), unique=False, nullable=False)
    favorite_planets = db.relationship('FavoritePlanets', backref= 'planets', lazy=True)

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "surface": self.surface,
            "diameter": self.diameter
        }

class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    passengers = db.Column(db.String(80), unique=False, nullable=False)
    length = db.Column(db.String(80), unique=False, nullable=False)
    cargo_capacity = db.Column(db.String(80), unique=False, nullable=False)
    favorite_vehicles = db.relationship('FavoriteVehicles', backref= 'vehicles', lazy=True)

    def __repr__(self):
        return '<Vehicles %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "passengers": self.passengers,
            "length": self.length,
            "cargo_capacity": self.cargo_capacity
        }

class FavoritePeople (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "people_id": self.people_id,
            "user_id": self.user_id,
            "people_name": People.query.get(self.people_id).serialize()["name"],
            "user_name": User.query.get(self.user_id).serialize()["name"],
            "user":User.query.get(self.user_id).serialize(),
            "people":People.query.get(self.people_id).serialize()
        }

class FavoritePlanets (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "planet_id": self.planet_id,
            "user_id": self.user_id,
            "planet_name": Planets.query.get(self.planet_id).serialize()["name"],
            "user_name": User.query.get(self.user_id).serialize()["name"],
            "user":User.query.get(self.user_id).serialize(),
            "planet":Planets.query.get(self.planet_id).serialize()
        }

class FavoriteVehicles (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "vehicle_id": self.vehicle_id,
            "user_id": self.user_id,
            "vehicle_name": Vehicles.query.get(self.vehicle_id).serialize()["name"],
            "user_name": User.query.get(self.user_id).serialize()["name"],
            "user":User.query.get(self.user_id).serialize(),
            "vehicle":Vehicles.query.get(self.vehicle_id).serialize()
        }

class TokenBlockedList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(250), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def serialize(self):
        return {
            "id":self.id,
            "token":self.token,
            "email":self.email,
            "created":self.created_at
        }