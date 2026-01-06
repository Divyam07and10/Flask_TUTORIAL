from app.models.user import User
from app.repositories import user_repository as repo
from app.core.security import hash_password, verify_password

def create_user(data):
    hashed = hash_password(data.password)
    user = User(
        username=data.username,
        email=data.email,
        password_hash=hashed
    )
    return repo.add_user(user)

def get_user(user_id):
    return repo.get_user_by_id(user_id)

def get_all_users():
    return repo.get_all_users()

def get_by_username(username):
    return repo.get_user_by_username(username)

def update_user(user, data):
    if not verify_password(data.current_password, user.password_hash):
        raise ValueError("Incorrect current password")

    update_data = data.model_dump(exclude_unset=True)
    
    if "username" in update_data:
        user.username = update_data["username"]
    
    if "new_password" in update_data:
        user.password_hash = hash_password(update_data["new_password"])
    
    repo.commit_changes()
    return user

def delete_user(user):
    repo.soft_delete_user(user)
