from datetime import date
from pydantic import BaseModel

class EventBase(BaseModel):
    name: str
    date: date
    location: str

class EventCreate(EventBase):
    pass

class EventUpdate(EventBase):
    pass

class Event(EventBase):
    id: int

    class Config:
        orm_mode = True
