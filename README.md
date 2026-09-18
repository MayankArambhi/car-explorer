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
│   ├── __init__.py
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

## How to run locally

1. Clone the repository:
   ```bash
   git clone https://github.com/MayankArambhi/car-explorer.git
   cd car-explorer
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create environment file:
    - Create ```.env``` file inside ```/application```.
    - Add variable ```SECRET_KEY``` and assign it a string.

5. Run the app:
   ```bash
   python app.py
   ```

6. Open in browser:
http://127.0.0.1:5000