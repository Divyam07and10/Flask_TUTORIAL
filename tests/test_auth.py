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
    assert "access_token" in response.json
    assert "refresh_token" in response.json

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
    refresh_token = login_res.json["refresh_token"]
    
    refresh_res = client.post('/api/auth/refresh', headers={
        "Authorization": f"Bearer {refresh_token}"
    })
    assert refresh_res.status_code == 200
    assert "access_token" in refresh_res.json
