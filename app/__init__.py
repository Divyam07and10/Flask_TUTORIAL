from flask import Flask
from app.core.config import Config
from app.extensions import db, migrate, jwt, bcrypt

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)
    
    @app.route('/')
    def index():
        return "Hellp, Flask Boilerplate is running!"

    return app
