from pydantic import BaseModel

class ContactBase(BaseModel):
    name: str
    email: str
    phone: str = None
    company: str = None

class ContactCreate(ContactBase):
    pass

class ContactUpdate(ContactBase):
    pass

class Contact(ContactBase):
    id: int

    class Config:
        orm_mode = True

class ContactList(BaseModel):
    contacts: list[Contact]
