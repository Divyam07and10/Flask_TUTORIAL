import os
from flask import Flask
from app.core.config import Config
from app.extension import db, migrate, jwt, bcrypt, cors
from app.api.auth import auth_bp
from app.api.users import users_bp

def createApp(testing=False) -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    cors.init_app(app, origins=app.config.get('CORS_ORIGINS'), supports_credentials=True)

    if testing:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = app.config.get("SQLALCHEMY_TESTING_DATABASE_URI")
        app.config["WTF_CSRF_ENABLED"] = False

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(users_bp, url_prefix='/api/users')

    return app
