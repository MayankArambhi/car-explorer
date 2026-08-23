from flask import render_template, request
from application import app
from application.database import db
from application.models import Cars, Brands

@app.route("/")
def home():
    sort = request.args.get("sort", "")
    search = request.args.get("search", "").strip()
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
    return render_template("index.html", cars=cars, search=search, number = l)

@app.route("/car/<int:car_id>")
def car(car_id):
    car = db.session.execute(db.text(f"""
    select *
    from cars natural join brands
    where cars.car_id= :car_id
"""), {"car_id":car_id}).first()
    print(car.car_name)
    return render_template("car.html", car=car)