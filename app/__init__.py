from flask import Flask

def create_app():
    app = Flask(__name__)

    # configuración opcional
    # app.config["DEBUG"] = True
    app.config.from_mapping(
        DEBUG = True
    )

    # registro de blueprints
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
