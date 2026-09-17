# Car explorer
A full stack web application as a Flask learner.

## Tech stack
- Python
- Flask
- SQLAlchemy
- SQLite
- DBeaver
- HTML
- CSS
- Werkzeug (for password hashing)

## Features
- Authentication
    - Sign up
    - Login
    - Logout
    - Password hashing
- Car listing with basic info
- Individual car page
- Individual brand page
- Sorting by price, safety ratings, sales

## File Structure
```
car-explorer/
├── application/
│   ├── database/
│   |   └── carsdb
│   ├── init.py
│   ├── config.py
│   ├── controllers.py
│   ├── database.py
│   └── models.py
├── static/
│   ├── media/cars/ (contains images of cars)
│   └── styles/
|       └── style.css
├── templates/
│   ├── auth.html
│   ├── brand.html
│   ├── car.html
│   └── index.html
├── app.py
└── requirements.txt
```