from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Joblinks(db.Model):
    __tablename__ = 'job_link'
    _ = db.Column(db.Integer, primary_key=True)
    url_id = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)