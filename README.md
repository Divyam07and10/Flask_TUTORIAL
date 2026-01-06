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

## 📡 API Documentation
Use the included `postman_collection.json` to interact with the API endpoints:
- **Auth**: `/api/auth/register`, `/api/auth/login`
- **Users**: `/api/users/` (Full CRUD)

## 📂 Project Structure
- `app/api/`: Modular Blueprints for Auth and User management.
- `app/core/`: Configuration and Security logic.
- `app/models/`: SQLAlchemy database models.
- `app/repositories/`: Pure functional database operations.
- `app/services/`: Functional business logic.
- `app/schemas/`: Pydantic models for request/response validation.
- `app/utils/`: Security and configuration utilities.
- `tests/`: Isolated unit tests using in-memory database.
