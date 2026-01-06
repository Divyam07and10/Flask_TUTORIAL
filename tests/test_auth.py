import json

def test_user_registration(client):
    response = client.post('/api/auth/register', json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "Password123!"
    })
    assert response.status_code == 201
    assert "User created successfully" in response.get_json()['msg']

def test_user_login(client):
    client.post('/api/auth/register', json={
        "username": "logintest",
        "email": "login@example.com",
        "password": "Password123!"
    })
    
    response = client.post('/api/auth/login', json={
        "username": "logintest",
        "password": "Password123!"
    })
    assert response.status_code == 200
    assert "access_csrf" in response.json
    assert "refresh_csrf" in response.json

def test_user_refresh(client):
    client.post('/api/auth/register', json={
        "username": "refreshtest",
        "email": "refresh@example.com",
        "password": "Password123!"
    })
    
    login_res = client.post('/api/auth/login', json={
        "username": "refreshtest",
        "password": "Password123!"
    })
    refresh_csrf = login_res.json["refresh_csrf"]
    
    refresh_res = client.post('/api/auth/refresh', headers={"X-CSRF-TOKEN": refresh_csrf})
    assert refresh_res.status_code == 200
    assert "access_csrf" in refresh_res.json

def test_user_logout(client):
    client.post('/api/auth/register', json={
        "username": "logouttest",
        "email": "logout@example.com",
        "password": "Password123!"
    })
    
    login_res = client.post('/api/auth/login', json={
        "username": "logouttest",
        "password": "Password123!"
    })
    access_csrf = login_res.json["access_csrf"]
    
    logout_res = client.post('/api/auth/logout', headers={"X-CSRF-TOKEN": access_csrf})
    assert logout_res.status_code == 200
    
    res = client.get('/api/users/me')
    assert res.status_code == 401
