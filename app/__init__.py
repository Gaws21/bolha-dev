from flask import Flask

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    
    with app.app_context():
        # Import parts of our core Flask app
        from . import routes
        return app