import pytest
from fastapi.testclient import TestClient
from app import app
from models import Event, User
from database import get_db

from jose import jwt
from config import SECRET_KEY, ALGORITHM
from datetime import datetime, timedelta
from passlib.context import CryptContext

client = TestClient(app)

@pytest.fixture(scope="module")
def test_db():
    db = next(get_db())
    yield db
    db.rollback()

def test_add_event_to_lead(test_db):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    user_db = User(email="test@example.com", hashed_password=pwd_context.hash("testpassword"))
    test_db.add(user_db)
    test_db.commit()
    test_db.refresh(user_db)
    test_db.close()
        
    access_token_expires = timedelta(minutes=30)
    user_id = 1
    token_data = {
        "sub": str(user_id),
        "scopes": ["event:create"],
        "exp": datetime.utcnow() + access_token_expires
    }
    token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
    headers = {"Authorization": f"Bearer {token}"}    
    
    data = {
        "title": "New Event",
        "description": "This is a new event",
        "start_time": "2023-03-01 10:00:00",
        "end_time": "2023-03-01 12:00:00"
    }
    response = client.post("/events/", headers=headers, json=data)

    # Check that the event was created successfully
    assert response.status_code == 200
    event = response.json()
    assert event["title"] == "New Event"
    assert event["description"] == "This is a new event"
    assert event["start_time"] == "2023-03-01T10:00:00"
    assert event["end_time"] == "2023-03-01T12:00:00"

    # Delete the event to clean up the database
    test_db.delete(test_db.query(Event).filter_by(id=event["id"]).first())
    test_db.commit()
    
    # # create a user
    # user_data = {"email": "testuser@example.com", "password": "testpassword"}
    # user_create = UserCreate(**user_data)
    # response = client.post("/users/", data=user_create.json())
    # assert response.status_code == 201
    # user_id = response.json()["id"]

    # # create a lead
    # lead_data = {"first_name": "John", "last_name": "Doe", "email": "johndoe@example.com", "user_id": user_id}
    # lead_create = LeadCreate(**lead_data)
    # response = client.post("/leads/", data=lead_create.json())
    # assert response.status_code == 201
    # lead_id = response.json()["id"]

    # # create an event
    # event_data = {"name": "Test Event", "description": "A test event", "lead_id": lead_id}
    # event_create = EventCreate(**event_data)
    # response = client.post("/events/", data=event_create.json())
    # assert response.status_code == 201
    # event_id = response.json()["id"]

    # # get the lead and check that the event is in the events list
    # response = client.get(f"/leads/{lead_id}")
    # assert response.status_code == 200
    # lead = response.json()
    # assert lead["id"] == lead_id
    # assert lead["events"] == [{"id": event_id, "name": "Test Event", "description": "A test event", "lead_id": lead_id}]