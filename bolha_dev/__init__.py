from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

BASE_DIR = '/home/linkedin-python-scrapy-scraper'
db = SQLAlchemy()
app = Flask(__name__)
db_name = 'database.db'
db_path = os.path.join(BASE_DIR, db_name)
db_path = "/home/linkedin-python-scrapy-scraper/myjobs.db"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)

class Joblinks(db.Model):
    __tablename__ = 'job_link'
    _ = db.Column(db.Integer, primary_key=True)
    job_link = db.Column(db.String(100), nullable=False)
    job_name = db.Column(db.String(100), nullable=False)

def init_app():

    with app.app_context():
        # Import parts of our core Flask app
        from . import routes

        return app