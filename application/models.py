from application.database import db

class Brands(db.Model):
    __tablename__ = 'brands'
    brand_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    brand_name = db.Column(db.String, nullable=False)

class Cars(db.Model):
    __tablename__ = 'cars'
    car_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    brand_id = db.Column(db.Integer, db.ForeignKey('brands.brand_id'))
    car_name = db.Column(db.String, nullable=False)
    type = db.Column(db.String)
    launch_date = db.Column(db.Integer)
    safety_rating = db.Column(db.Float)
    sales_count = db.Column(db.Integer)
    price = db.Column(db.Integer)
    image = db.Column(db.String)