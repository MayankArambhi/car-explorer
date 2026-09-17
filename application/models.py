from application.database import db

class Brands(db.Model):
    __tablename__ = 'brands'
    brand_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    brand_name = db.Column(db.String, nullable=False)

class Cars(db.Model):
    __tablename__ = 'cars'
    car_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    car_name = db.Column(db.String, nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('brands.brand_id'))
    type_id = db.Column(db.Integer, db.ForeignKey('types.type_id'))
    images = db.relationship("Images", backref="car", lazy=True)
    brand = db.relationship("Brands", backref="cars")
    type = db.relationship("Types", backref="car")
    launch_date = db.Column(db.Integer)
    safety_rating = db.Column(db.Float)
    sales_count = db.Column(db.Integer)
    price = db.Column(db.Integer)

class Images(db.Model):
    __tablename__ = 'images'
    image_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    car_id = db.Column(db.Integer, db.ForeignKey('cars.car_id'))
    path = db.Column(db.String)

class Types(db.Model):
    __tablename__ = 'types'
    type_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    type_name = db.Column(db.String)

class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)