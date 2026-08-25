from flask import render_template, request, redirect
from application import app
from application.database import db

@app.route("/")
def home():
    sort = request.args.get("sort", "")
    search = request.args.get("search", "").strip()
    for char in ["<", ">", '=']:
        if char in search:
            search=""
            break
    query = """
        select * from
        cars natural join brands 
    """
    if sort:
        if sort=="price-asc":
            query += "order by price asc"
        elif sort=="price-desc":
            query += "order by price desc"
        elif sort=="safety":
            query += "order by safety_rating desc"
        elif sort=="sales":
            query += "order by sales_count desc"
    elif search:
        query += f"where car_name like '%{search}%' or brand_name like '%{search}%'"
    
    cars = db.session.execute(db.text(query)).all()
    l = len(list(cars))
    return render_template("index.html", cars=cars, search=search, sort=sort, number = l)

@app.route("/car/<int:car_id>")
def car(car_id):
    car = db.session.execute(db.text(f"""
        select *
        from cars natural join brands
        where cars.car_id = :car_id
    """), {"car_id":car_id}).first()
    print(car.car_name)
    return render_template("car.html", car=car)

@app.route("/brand/<int:brand_id>")
def brand(brand_id):
    sort = request.args.get("sort", "")
    search = request.args.get("search", "").strip()
    for char in ["<", ">", '=']:
        if char in search:
            search=""
            break
    query = """
        select * from
        cars natural join brands
        where cars.brand_id = :brand_id 
    """
    if sort:
        if sort=="price-asc":
            query += "order by price asc"
        elif sort=="price-desc":
            query += "order by price desc"
        elif sort=="safety":
            query += "order by safety_rating desc"
        elif sort=="sales":
            query += "order by sales_count desc"
    elif search:
        query += f"and car_name like '%{search}%'"
    
    cars = db.session.execute(db.text(query), {"brand_id": brand_id}).all()
    l = len(list(cars))
    brand_name = cars[0].brand_name
    return render_template("brand.html", cars=cars, search=search, number = l, brand_name=brand_name, brand_id=brand_id)