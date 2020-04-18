from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(25), nullable=False, unique=True)
    name = db.Column(db.String(35), nullable=False)

    booking_user = db.relationship('Book', backref='user', lazy=True)

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    address = db.Column(db.String(50), nullable=False)

    restaurant_table = db.relationship('Restaurant_Tables', backref='restaurant', lazy=True)
    booking_restaurant = db.relationship('Book', backref='restaurant', lazy=True)
    restaurant_menu = db.relationship('Menu', backref='restaurant', lazy=True)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id' : self.id,
            'name' : self.name,
            'address' : self.address
        }

class Restaurant_Tables(db.Model):
    __tablename__ = 'restaurant_tables'
    id=db.Column(db.Integer, primary_key=True)
    number=db.Column(db.Integer, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id', ondelete='CASCADE'),nullable=False)
    availability = db.Column(db.Boolean(),default=True)
    occupancy = db.Column(db.Integer)

    booking_table = db.relationship('Book', backref='restaurant_tables', lazy=True)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        restaurant = Restaurant.query.filter_by(id = self.restaurant_id).first()
        return {
            'id' : self.id,
            'number' : self.number,
            'restaurant' : restaurant.name + ", " + restaurant.address,
            'availability' : self.availability,
            'occupancy' : self.occupancy
        }

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id', ondelete='CASCADE'), nullable=False)
    price = db.Column(db.Integer)

class Book(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id', ondelete='CASCADE'), nullable=False)
    table_id = db.Column(db.Integer, db.ForeignKey('restaurant_tables.id', ondelete='CASCADE'), nullable=False)
    no_of_guests = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    reserved_date = db.Column(db.DateTime)
    bill = db.Column(db.Integer, nullable=False)