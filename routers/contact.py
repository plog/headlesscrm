from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.contact import Contact
from schemas.contact import ContactCreate, ContactUpdate
from database import get_db

router = APIRouter()

@router.post("/contacts")
def create_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    db_contact = Contact(name=contact.name, email=contact.email)
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

@router.get("/contacts")
def read_contacts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    contacts = db.query(Contact).offset(skip).limit(limit).all()
    return contacts

@router.get("/contacts/{contact_id}")
def read_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

@router.put("/contacts/{contact_id}")
def update_contact(contact_id: int, contact: ContactUpdate, db: Session = Depends(get_db)):
    db_contact = db.query(Contact).filter(Contact.id == contact_id)
    if not db_contact.first():
        raise HTTPException(status_code=404, detail="Contact not found")
    db_contact.update(contact.dict())
    db.commit()
    return {"message": "Contact updated successfully"}

@router.delete("/contacts/{contact_id}")
def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    db_contact = db.query(Contact).filter(Contact.id == contact_id)
    if not db_contact.first():
        raise HTTPException(status_code=404, detail="Contact not found")
    db_contact.delete(synchronize_session=False)
    db.commit()
    return {"message": "Contact deleted successfully"}
