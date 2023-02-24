from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from database import Base


contact_events = Table(
    "contact_events",
    Base.metadata,
    Column("contact_id", Integer, ForeignKey("contacts.id")),
    Column("event_id", Integer, ForeignKey("events.id")),
)

lead_events = Table(
    "lead_events",
    Base.metadata,
    Column("lead_id", Integer, ForeignKey("leads.id")),
    Column("event_id", Integer, ForeignKey("events.id")),
)


class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, index=True)

    events = relationship(
        "Event", secondary=contact_events, back_populates="contacts"
    )


class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, index=True)
    company = Column(String, index=True)
    is_qualified = Column(Boolean, default=False)

    events = relationship("Event", secondary=lead_events, back_populates="leads")


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    start_time = Column(String, index=True)
    end_time = Column(String, index=True)

    contacts = relationship(
        "Contact", secondary=contact_events, back_populates="events"
    )

    leads = relationship("Lead", secondary=lead_events, back_populates="events")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
