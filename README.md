# Car explorer
A full stack web application as a Flask learner.

[Click here](https://car-explorer.onrender.com) for live demo.

## Features
- Authentication
    - Sign up
    - Login
    - Logout
    - Password hashing
- Cars listed with...
    - Image
    - Model & Brand name
    - Price
    - Safety rating
    - Sales
    - Launch year
- Individual car page
- Individual brand page
- Search keywords
- Sort by...
    - Price
    - Safety ratings
    - Sales

## Tech stack
- Python
- Flask
- SQLAlchemy
- SQLite
- DBeaver
- HTML
- CSS
- Werkzeug (for password hashing)

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