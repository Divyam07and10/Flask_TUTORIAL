import os
from dotenv import load_dotenv
from app.utils.config_utils import parse_time

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-123')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATION', 'False') == 'True'
    
    JWT_SECRET_KEY = os.getenv('ACCESS_TOKEN_SECRET', 'jwt-dev-key')
    JWT_REFRESH_SECRET_KEY = os.getenv('REFRESH_TOKEN_SECRET', 'jwt-refresh-dev-key')
    JWT_ALGORITHM = os.getenv('JWT_ALGO', 'HS256')
    JWT_TOKEN_LOCATION = os.getenv('JWT_LOCATION', 'headers').split(',')
    
    JWT_ACCESS_TOKEN_EXPIRES = parse_time(os.getenv('ACCESS_TOKEN_EXPIRE_TIME', '30m'))
    JWT_REFRESH_TOKEN_EXPIRES = parse_time(os.getenv('REFRESH_TOKEN_EXPIRE_TIME', '1d'))

    SQLALCHEMY_TESTING_DATABASE_URI = os.getenv('SQLALCHEMY_TESTING_DATABASE_URI', 'sqlite:///:memory:')
