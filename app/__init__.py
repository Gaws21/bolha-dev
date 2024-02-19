from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
class Joblinks(db.Model):
    __tablename__ = 'job_link'
    _ = db.Column(db.Integer, primary_key=True)
    url_id = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    
    db.init_app(app)
    with app.app_context():
        # Import parts of our core Flask app
        from . import routes
        return app