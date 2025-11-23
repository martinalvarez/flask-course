from flask import Flask
from .core.config import load_config

def create_app():
    app = Flask(__name__)

    # Load environment variables, config, and SECRET_KEY
    load_config(app)

    # Register blueprints
    from .routes import main_bp
    app.register_blueprint(main_bp)

    from .auth.routes import auth_bp
    app.register_blueprint(auth_bp)

    return app
