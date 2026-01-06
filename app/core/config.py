import os
from dotenv import load_dotenv
from app.utils.config_utils import parse_time

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-123')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', 'False') == 'True'
    
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwt-dev-key')
    JWT_REFRESH_SECRET_KEY = os.getenv('JWT_REFRESH_SECRET_KEY', 'jwt-refresh-dev-key')
    JWT_ALGORITHM = os.getenv('JWT_ALGORITHM', 'HS256')
    JWT_COOKIE_SECURE = os.getenv('JWT_COOKIE_SECURE', 'False') == 'True'
    JWT_TOKEN_LOCATION = os.getenv('JWT_TOKEN_LOCATION', 'cookies').split(',')
    JWT_COOKIE_CSRF_PROTECT = os.getenv('JWT_COOKIE_CSRF_PROTECT', 'True') == 'True'
    JWT_ACCESS_COOKIE_PATH = os.getenv('JWT_ACCESS_COOKIE_PATH', '/api')
    JWT_REFRESH_COOKIE_PATH = os.getenv('JWT_REFRESH_COOKIE_PATH', '/api/auth/refresh')
    JWT_COOKIE_SAMESITE = os.getenv('JWT_COOKIE_SAMESITE', 'Lax')
    
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', 'http://localhost:3000').split(',')
    
    JWT_ACCESS_TOKEN_EXPIRES = parse_time(os.getenv('ACCESS_TOKEN_EXPIRE_TIME', '30m'))
    JWT_REFRESH_TOKEN_EXPIRES = parse_time(os.getenv('REFRESH_TOKEN_EXPIRE_TIME', '1d'))

    SQLALCHEMY_TESTING_DATABASE_URI = os.getenv('SQLALCHEMY_TESTING_DATABASE_URI', 'sqlite:///:memory:')
