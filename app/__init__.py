from flask import Flask
from .site.routes import site_bp
from .api.routes import api_bp
from flask_bootstrap import Bootstrap

def create_app():
    app = Flask(__name__)
    Bootstrap(app)

    app.register_blueprint(site_bp)
    app.register_blueprint(api_bp)

    return app