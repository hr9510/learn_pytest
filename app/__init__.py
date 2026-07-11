from flask import Flask
from app.extensions.extensions import db, jwt
from app.configuration.configuration import Testing_Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Testing_Config)

    db.init_app(app)
    jwt.init_app(app, db)

    from app.routes.user_routes import main_bp
    app.register_blueprint(main_bp)
    return app


