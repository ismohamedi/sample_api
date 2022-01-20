from datetime import datetime
from typing import List
from pydantic import BaseModel

# create base schema
class ContactBase(BaseModel):
    first_name: str
    last_name: str
    organisation: str
    phone_number: str


# schema for contact creaton
class ContactCreate(ContactBase):
    pass


class Contact(ContactBase):
    id: int
    created_on: datetime

    class Config:
        orm_mode = True
