from flask import Flask


def init_app():
    app = Flask(__name__)

    with app.app_context():
        # Import parts of our core Flask app
        from . import routes
        
        # Import Dash application
        from .dashboard import init_dashboard

        app = init_dashboard(app)

        return app