from pydantic import BaseModel
from typing import Optional

class EventBase(BaseModel):
    title: str
    description: str

class EventCreate(EventBase):
    contact_id: Optional[int] = None
    lead_id: Optional[int] = None

class EventUpdate(EventBase):
    pass

class Event(EventBase):
    id: int
    contact_id: Optional[int] = None
    lead_id: Optional[int] = None

    class Config:
        orm_mode = True

class EventList(BaseModel):
    events: list[Event]
