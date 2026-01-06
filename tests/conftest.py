import pytest
from app import createApp
from app.extension import db

@pytest.fixture
def client():
    app = createApp(testing=True)

    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()
