from pydantic import BaseModel

class LeadBase(BaseModel):
    name: str
    email: str

class LeadCreate(LeadBase):
    pass

class LeadUpdate(LeadBase):
    pass

class Lead(LeadBase):
    id: int

    class Config:
        orm_mode = True
