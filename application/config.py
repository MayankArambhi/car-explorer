import os

cd = os.path.abspath(os.path.dirname(__file__))
PASSWORD=os.environ["PASSWORD"].replace("@","%40")
PORT=os.environ["PORT"]

class Config:
    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://postgres:{PASSWORD}@localhost:{PORT}/carsdb"