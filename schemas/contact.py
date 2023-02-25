from pydantic import BaseModel

class ContactBase(BaseModel):
    first_name: str
    last_name: str
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
