from flask import Flask
from app.config import ProductionConfig

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    
    with app.app_context():
        from . import routes
        return app
