import json

def test_get_users_unauthorized(client):
    response = client.get('/api/users/')
    assert response.status_code == 401

def test_user_crud_cycle(client):
    client.post('/api/auth/register', json={
        "username": "cruduser",
        "email": "crud@example.com",
        "password": "Password123!"
    })
    
    login_res = client.post('/api/auth/login', json={
        "username": "cruduser",
        "password": "Password123!"
    })
    token = login_res.get_json()['access_token']
    headers = {'Authorization': f'Bearer {token}'}
    
    me_res = client.get('/api/users/me', headers=headers)
    assert me_res.status_code == 200
    user_id = me_res.get_json()['id']
    
    update_res = client.put(f'/api/users/{user_id}', headers=headers, json={
        "current_password": "Password123!",
        "username": "updated_cruduser"
    })
    assert update_res.status_code == 200
    assert update_res.get_json()['username'] == "updated_cruduser"
    
    del_res = client.delete(f'/api/users/{user_id}', headers=headers)
    assert del_res.status_code == 200
    
    verify_res = client.get(f'/api/users/{user_id}', headers=headers)
    assert verify_res.status_code == 404
