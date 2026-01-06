# Professional Flask User CRUD Boilerplate

A production-grade, minimalist Flask application featuring a functional architecture, Pydantic validation, JWT authentication, and automated testing.

## 🚀 Quick Start

### 1. Environment Setup
Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configuration
Copy the example environment file and configure your credentials:
```bash
cp .env.example .env
```
Ensure your `.env` contains:
- `SECRET_KEY`
- `SQLALCHEMY_DATABASE_URI` (PostgreSQL/SQLite)
- `ACCESS_TOKEN_SECRET`
- `REFRESH_TOKEN_SECRET`
- `ACCESS_TOKEN_EXPIRE_TIME` (e.g., 30m, 1h)
- `REFRESH_TOKEN_EXPIRE_TIME` (e.g., 1d, 7d)
- `SQLALCHEMY_TESTING_DATABASE_URI` (sqlite:///:memory:)

### 3. Database Migrations
Initialize the database and apply migrations:
```bash
export FLASK_APP=app:createApp
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### Development Mode (Simplified)
With `.flaskenv` configured, you can use:
```bash
flask run
```
*Reloads automatically on port 5000 (via watchdog).*

*Direct python run:*
```bash
python app.py
```

### Production Mode (Gunicorn)
```bash
# Gunicorn defaults to port 8000. Use -b to bind to 5000:
gunicorn -w 4 -b 0.0.0.0:5000 app:create_app()
```

## 🧪 Testing
Run the complete unit test suite:
```bash
python3 -m pytest -vv
```

## 🧪 API Interaction

This project uses secure **HttpOnly cookies** for authentication.

1.  **Login**: Call `POST /api/auth/login`. The server will set `access_token_cookie` and `refresh_token_cookie`.
2.  **Authenticated Requests**: In Postman or your browser, these cookies are sent automatically. No manual `Authorization` header is required.
3.  **Refresh**: Call `POST /api/auth/refresh` when the access token expires.
4.  **Logout**: Call `POST /api/auth/logout` to clear all security cookies.

### Postman Setup
- Import `postman_collection.json`.
- Set the `user_id` variable after your first login.
- Cookies will be managed automatically in the Postman "Cookies" tab.
- `app/services/`: Functional business logic.
- `app/schemas/`: Pydantic models for request/response validation.
- `app/utils/`: Security and configuration utilities.

## 🏁 Operational Status
- **Auth**: Cookie-based JWT (Secure/HttpOnly)
- **Database**: PostgreSQL / SQLAlchemy
- **Migration**: Flask-Migrate
- **Testing**: 100% Pass Rate (pytest)
- `tests/`: Isolated unit tests using in-memory database.
