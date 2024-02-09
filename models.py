from os import environ
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Payroll(db.Model):

    __extends_existing__ = True

    __tablename__ = "payroll"

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(4), nullable=False)
    usd = db.Column(db.String, nullable=False)
    district = db.Column(db.Text, nullable=False)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    position = db.Column(db.Text, nullable=False)
    total_pay = db.Column(db.Text, nullable=False)


def connect_to_database(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = environ["POSTGRES_URI"]
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    print("Connected to database!")

if __name__ == "__main__":
    from app import app
    connect_to_database(app)
    print("Connected to database!")