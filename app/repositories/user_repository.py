from app.models.user import User
from app.extension import db

def get_all_users():
    return User.query.all()

def get_user_by_id(user_id):
    return User.query.filter_by(id=user_id, is_active=True).first()

def get_user_by_username(username):
    return User.query.filter_by(username=username, is_active=True).first()

def get_user_by_email(email):
    return User.query.filter_by(email=email, is_active=True).first()

def add_user(user):
    db.session.add(user)
    db.session.commit()
    return user

def commit_changes():
    db.session.commit()

def soft_delete_user(user):
    user.is_active = False
    db.session.commit()
