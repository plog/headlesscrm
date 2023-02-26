import json
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app import app
from models import Contact
from database import get_db

client = TestClient(app)

@pytest.fixture(scope="module")
def test_db():
    db = next(get_db())
    yield db
    db.rollback()

def test_list_all_contacts(test_db):
    contact_to_delete = test_db.query(Contact).filter(
        Contact.first_name == "John", 
        Contact.last_name == "Doe").first()
    
    if contact_to_delete:
        test_db.delete(contact_to_delete)
        test_db.commit()
        
    response = client.get("/contacts")
    assert response.status_code == 200

    # Insert 
    contact_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "johndoe@example.com",
        "phone": "555-1234"
    }
    response = client.post("/contacts", json=contact_data)

    response = client.get("/contacts")
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()[0]["first_name"] == "John"
    assert response.json()[0]["last_name"] == "Doe"
    assert response.json()[0]["email"] == "johndoe@example.com"
    assert response.json()[0]["phone"] == "555-1234"
