from fastapi.testclient import TestClient

from main import app
from database import db

client = TestClient(app)


def test_create_volunteer():
    db.clear()
    response = client.post("/volunteer", json={
        "nome": "Douglas",
        "email": "douglas@email.com",
        "cargo_pretendido": "Backend Jr",
        "disponibilidade": "manha"
    })
    assert response.status_code == 200
    assert response.json()["nome"] == "Douglas"
    
    
def test_add_volunteer_error_422():
    db.clear()
    response = client.post("/volunteer", json={
        "nome": "Douglas",
        "email": "sdlfakdfkjl",
        "cargo_pretendido": "Backend Jr",
        "disponibilidade": "manha"
    })    
    assert response.status_code == 422
    detail = response.json()["detail"]
    assert any(err["loc"][-1] == "email" for err in detail)


def test_create_volunteer_error_422():
    db.clear()
    response = client.post("/volunteer", json={
        "nome": "Douglas",
        "email": "douglas@email.com",
        "cargo_pretendido": "Backend Jr"
    })
    assert response.status_code == 422
    
    detail = response.json()["detail"]
    assert any(err["loc"][-1] == "disponibilidade" for err in detail)
    

def test_create_volunteer_error_400():
    db.clear()
    first_response = client.post("/volunteer", json={
        "nome": "Douglas",
        "email": "douglas@email.com",
        "cargo_pretendido": "Backend Jr",
        "disponibilidade": "manha"
    })
    
    second_response = client.post("/volunteer", json={
        "nome": "Douglas",
        "email": "douglas@email.com",
        "cargo_pretendido": "Backend Jr",
        "disponibilidade": "manha"
    })
    
    assert second_response.status_code == 400
    assert second_response.json()["detail"] == "Email already exists"


def test_list_volunteer():
    db.clear()
    first_response = client.post("/volunteer", json={
        "nome": "Douglas",
        "email": "douglas@email.com",
        "cargo_pretendido": "Backend Jr",
        "disponibilidade": "manha"
    })
    
    second_response = client.get("/volunteer", params={
        "status": True,
        "disponibilidade": "manha"
    })

    assert second_response.status_code == 200
    data = second_response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert data[0]["nome"] == "Douglas"
    
    
def test_list_volunteer_error_404():
    db.clear()
    response = client.get("/volunteer", params={
        "status": False,
        "disponibilidade": "tarde"
    })
    print(response)

    assert response.status_code == 404
    assert response.json()["detail"] == "Not found"



def test_get_volunteer():
    db.clear()
    first_response = client.post("/volunteer", json={
        "nome": "Douglas",
        "email": "douglas@email.com",
        "cargo_pretendido": "Backend Jr",
        "disponibilidade": "manha"
    })
    
    second_response = client.get("/volunteer/1")

    assert second_response.status_code == 200
    assert second_response.json()["nome"] == "Douglas"


def test_get_volunteer_error_404():
    db.clear()
    response = client.get("/volunteer/0")

    assert response.status_code == 404
    assert response.json()["detail"] == "Not found"
    

def test_update_volunteer():
    db.clear()
    first_response = client.post("/volunteer", json={
        "nome": "Douglas",
        "email": "douglas@email.com",
        "cargo_pretendido": "Backend Jr",
        "disponibilidade": "manha"
    })
    
    second_response = client.put(f"volunteer/{1}", json={
        "nome": "ed",
        "email": "ed@gmail.com",
        "cargo_pretendido": "Frontend Jr",
        "disponibilidade": "tarde",
    })
    
    assert second_response.status_code == 200
    assert second_response.json()["nome"] == "ed"
    assert second_response.json()["email"] == "ed@gmail.com"
    assert second_response.json()["cargo_pretendido"] == "Frontend Jr"
    assert second_response.json()["disponibilidade"] == "tarde"


def test_update_volunteer_error_422():
    db.clear()
    first_response = client.post("/volunteer", json={
        "nome": "Douglas",
        "email": "douglas@email.com",
        "cargo_pretendido": "Backend Jr",
        "disponibilidade": "manha"
    })
    
    second_response = client.put(f"/volunteer/1", json={
        "email": "fkldasfjkldaflksdf"
    })
    
    assert second_response.status_code == 422
    detail = second_response.json()["detail"]
    assert any(err["loc"][-1] == "email" for err in detail)


def test_update_volunteer_error_404():
    db.clear()
    response = client.put(f"/volunteer/1", json={
        "email": "douglas@gmail.com"
    })
    
    assert response.status_code == 404
    assert response.json()["detail"] == "Volunteer not found"


def test_delete_volunteer():
    db.clear()
    first_response = client.post("/volunteer", json={
        "nome": "Douglas",
        "email": "douglas@email.com",
        "cargo_pretendido": "Backend Jr",
        "disponibilidade": "manha"
    })
    
    second_response = client.delete(f"/volunteer/1")
    
    assert second_response.status_code == 200
    assert second_response.json()["nome"] == "Douglas"
    

def test_delete_volunteer_error_404():
    db.clear()
    response = client.delete(f"/volunteer/1")
    
    assert response.status_code == 404
    assert response.json()["detail"] == "Volunteer not found"