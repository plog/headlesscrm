from pydantic import BaseModel

class LeadBase(BaseModel):
    name: str
    email: str
    phone: str = None
    company: str = None

class LeadCreate(LeadBase):
    pass

class LeadUpdate(LeadBase):
    pass

class Lead(LeadBase):
    id: int

    class Config:
        orm_mode = True

class LeadList(BaseModel):
    leads: list[Lead]
