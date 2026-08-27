from flask import render_template, request, redirect
from application import app
from application.database import db
from sqlalchemy import or_
from application.models import Cars, Brands

@app.route("/")
def home():
    sort = request.args.get("sort", "")
    search = request.args.get("search", "").strip()
    for char in ["<", ">", '=']:
        if char in search:
            search=""
            break
    cars = Cars.query.all()
    if sort:
        if sort=="price-asc":
            cars = Cars.query.order_by(Cars.price.asc()).all()
        elif sort=="price-desc":
            cars = Cars.query.order_by(Cars.price.desc()).all()
        elif sort=="safety":
            cars = Cars.query.order_by(Cars.safety_rating.desc()).all()
        elif sort=="sales":
            cars = Cars.query.order_by(Cars.sales_count.desc()).all()
    elif search:
        cars = Cars.query.filter(
            or_(Cars.car_name.ilike(f"%{search}%"), 
                Cars.brand.has(Brands.brand_name.ilike(f"%{search}%"))
                )).all()

    l = len(cars)
    return render_template("index.html", cars=cars, search=search, sort=sort, number = l)

@app.route("/car/<int:car_id>")
def car(car_id):
    car = db.session.execute(db.text(f"""
        select *
        from cars natural join brands
        where cars.car_id = :car_id
    """), {"car_id":car_id}).first()
    return render_template("car.html", car=car)

@app.route("/brand/<int:brand_id>")
def brand(brand_id):
    sort = request.args.get("sort", "")
    search = request.args.get("search", "").strip()
    for char in ["<", ">", '=']:
        if char in search:
            search=""
            break

    cars = Cars.query.filter_by(brand_id=brand_id)
    brand = Brands.query.filter_by(brand_id=brand_id).first()
    
    if sort:
        if sort=="price-asc":
            cars = Cars.query.order_by(Cars.price.asc()).all()
        elif sort=="price-desc":
            cars = Cars.query.order_by(Cars.price.desc()).all()
        elif sort=="safety":
            cars = Cars.query.order_by(Cars.safety_rating.desc()).all()
        elif sort=="sales":
            cars = Cars.query.order_by(Cars.sales_count.desc()).all()
    elif search:
        cars = Cars.query.filter(
            or_(Cars.car_name.ilike(f"%{search}%"), 
                Cars.brand.has(Brands.brand_name.ilike(f"%{search}%"))
                )).all()
    
    l = len(list(cars))
    return render_template("brand.html", cars=cars, search=search, number = l, brand=brand)