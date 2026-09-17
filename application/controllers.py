from flask import render_template, session, request, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from application import app
from application.database import db
from sqlalchemy import or_
from application.models import Cars, Brands, Users

@app.route("/authentication")
def auth():
    return render_template("auth.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if '@' in username:
        print(username)
        user = Users.query.filter_by(email=username).first()
    else:
        user = Users.query.filter_by(username=username).first()
    if not user:
        # user not found
        return redirect(url_for("auth"))
    if check_password_hash(user.password, password):
        session["user_id"] = user.user_id
        return redirect(url_for("home"))

    return redirect(url_for("auth"))

@app.route("/signup", methods=["POST"])
def signup():
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    cpassword = request.form.get("conf-password")
    if password != cpassword:
        # password doesnt match confirm password
        return redirect(url_for("auth"))

    user = Users.query.filter_by(username = username).first()
    user2 = Users.query.filter_by(email=email).first()

    if user or user2:
        # username/email already exists
        return redirect(url_for("auth"))
    user = Users(
        username=username,
        email=email,
        password=generate_password_hash(
            password=password, 
            method="scrypt", 
            salt_length=16
            )
        )
    db.session.add(user)
    db.session.commit()
    user_id = user.user_id
    session["user_id"] = user_id

    return redirect(url_for("home"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth"))

@app.route("/")
def home():
    user_id = session.get("user_id", "")
    if not user_id:
        return redirect(url_for("auth"))
    
    sort = request.args.get("sort", "")
    search = request.args.get("search", "").strip()
    for char in ["<", ">", '=']:
        if char in search:
            search=""
            break
    query = Cars.query
    if search:
        query = query.filter(
            or_(Cars.car_name.ilike(f"%{search}%"), 
                Cars.brand.has(Brands.brand_name.ilike(f"%{search}%"))
                ))
    if sort=="price-asc":
        query = query.order_by(Cars.price.asc())
    elif sort=="price-desc":
        query = query.order_by(Cars.price.desc())
    elif sort=="safety":
        query = query.order_by(Cars.safety_rating.desc())
    elif sort=="sales":
        query = query.order_by(Cars.sales_count.desc())
    cars = query.all()

    l = len(cars)
    return render_template("index.html", cars=cars, search=search, sort=sort, number = l)

@app.route("/car/<int:car_id>")
def car(car_id):
    user_id = session.get("user_id", "")
    if not user_id:
        return redirect(url_for("auth"))
    car = db.session.execute(db.text(f"""
        select *
        from cars natural join brands
        where cars.car_id = :car_id
    """), {"car_id":car_id}).first()
    return render_template("car.html", car=car)

@app.route("/brand/<int:brand_id>")
def brand(brand_id):
    user_id = session.get("user_id", "")
    if not user_id:
        return redirect(url_for("auth"))
    sort = request.args.get("sort", "")
    search = request.args.get("search", "").strip()
    for char in ["<", ">", '=']:
        if char in search:
            search=""
            break
    query = Cars.query.filter_by(brand_id=brand_id)
    brand = Brands.query.filter_by(brand_id=brand_id).first()
    
    if search:
        query = query.filter(
            Cars.car_name.ilike(f"%{search}%"))
    if sort=="price-asc":
        query = query.order_by(Cars.price.asc())
    elif sort=="price-desc":
        query = query.order_by(Cars.price.desc())
    elif sort=="safety":
        query = query.order_by(Cars.safety_rating.desc())
    elif sort=="sales":
        query = query.order_by(Cars.sales_count.desc())
    cars = query.all()
    
    l = len(list(cars))
    return render_template("brand.html", cars=cars, search=search, number = l, brand=brand)