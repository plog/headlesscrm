from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Event
from schemas.event import EventCreate, EventUpdate
from database import get_db
from utils.auth import get_current_active_user  

router = APIRouter()

@router.post("/events")
def create_event(event: EventCreate, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    db_event = Event(name=event.name, date=event.date, location=event.location)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

@router.get("/events")
def read_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    events = db.query(Event).offset(skip).limit(limit).all()
    return events

@router.get("/events/{event_id}")
def read_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.put("/events/{event_id}")
def update_event(event_id: int, event: EventUpdate, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    db_event = db.query(Event).filter(Event.id == event_id)
    if not db_event.first():
        raise HTTPException(status_code=404, detail="Event not found")
    db_event.update(event.dict())
    db.commit()
    return {"message": "Event updated successfully"}

@router.delete("/events/{event_id}")
def delete_event(event_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    db_event = db.query(Event).filter(Event.id == event_id)
    if not db_event.first():
        raise HTTPException(status_code=404, detail="Event not found")
    db_event.delete(synchronize_session=False)
    db.commit()
    return {"message": "Event deleted successfully"}
