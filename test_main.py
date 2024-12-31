from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

def test_get_all_blogs():
    response = client.get("/blog/all")
    assert response.status_code == 200

def test_auth_error():
    response = client.post("/token",
      data={"username": "", "password": ""}, 
      headers={ 'Content-Type': 'application/x-www-form-urlencoded'}
    )
    assert response.status_code == 400
    assert response.text == '404: Invalid credentials'

def test_auth_success():
    response = client.post("/token",
      data={"username": "cat", "password": "cat"},
      headers={ 'Content-Type': 'application/x-www-form-urlencoded'}
    )
    print(response)
    access_token = response.json().get("access_token")
    print(access_token)
    assert access_token

def test_post_article():
    auth = client.post("/token",
      data={"username": "cat", "password": "cat"}
    )
    access_token = auth.json().get("access_token")
    
    assert access_token

    response = client.post(
        "/article/",
        json = {
            "title": "Test article",
            "content" : "Test content",
            "publish": True,
            "creator_id": 1
        },
        headers= {
            "Authorization" : "bearer " + access_token
        }
    )

    assert response.status_code == 200
    assert response.json().get("title") == "Test article" 
    