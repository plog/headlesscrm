from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.lead import Lead
from schemas.lead import LeadCreate, LeadUpdate
from database import get_db

router = APIRouter()

@router.post("/leads")
def create_lead(lead: LeadCreate, db: Session = Depends(get_db)):
    db_lead = Lead(name=lead.name, email=lead.email)
    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)
    return db_lead

@router.get("/leads")
def read_leads(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    leads = db.query(Lead).offset(skip).limit(limit).all()
    return leads

@router.get("/leads/{lead_id}")
def read_lead(lead_id: int, db: Session = Depends(get_db)):
    lead = db.query(Lead).filter(Lead.id == lead_id).first()
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    return lead

@router.put("/leads/{lead_id}")
def update_lead(lead_id: int, lead: LeadUpdate, db: Session = Depends(get_db)):
    db_lead = db.query(Lead).filter(Lead.id == lead_id)
    if not db_lead.first():
        raise HTTPException(status_code=404, detail="Lead not found")
    db_lead.update(lead.dict())
    db.commit()
    return {"message": "Lead updated successfully"}

@router.delete("/leads/{lead_id}")
def delete_lead(lead_id: int, db: Session = Depends(get_db)):
    db_lead = db.query(Lead).filter(Lead.id == lead_id)
    if not db_lead.first():
        raise HTTPException(status_code=404, detail="Lead not found")
    db_lead.delete(synchronize_session=False)
    db.commit()
    return {"message": "Lead deleted successfully"}
