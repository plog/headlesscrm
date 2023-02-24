import json
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app import app
from models import Contact

client = TestClient(app)

def test_list_all_contacts(db: Session):
    john_doe = Contact(
        first_name="John",
        last_name="Doe",
        email="johndoe@example.com",
        phone="555-1234")
    db.add(john_doe)
    db.commit()
        
    response = client.get("/contacts")
    assert response.status_code == 200
    assert len(response.json()) == 0  # assuming the database is empty

    # Assuming we have a contact in the database
    # You can replace the following lines with actual contact data
    contact_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "johndoe@example.com",
        "phone": "555-1234"
    }
    response = client.post("/contacts", json=contact_data)

    response = client.get("/contacts")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["first_name"] == "John"
    assert response.json()[0]["last_name"] == "Doe"
    assert response.json()[0]["email"] == "johndoe@example.com"
    assert response.json()[0]["phone"] == "555-1234"
