from ninja import Router
from core.views import *
from core import schema
from typing import List

#API router
api = Router()

@api.post("/add-contact", tags=["Create Contact"])
def add_contact(request, contact: schema.ContactCreate):
    return Contact.create_contact(request, contact)


@api.get("/get-contact", response=List[schema.Contact], tags=["Get Contacts"])
def get_contact(request):
    return Contact.get_contacts(request)
