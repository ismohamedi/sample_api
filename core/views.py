from django.shortcuts import render
from .models import Contact as contact_table

# Create your views here.


class Contact:
    def __init__(self):
        pass

    def create_contact(request, contact):
        try:
            if type(contact) != "dict":
                contact = contact.dict()
            contact = contact_table.objects.create(**contact)
            contact.save()
            if contact:
                return "contact saved"
            return {error: "failed to save"}
        except Exception as error:
            return str(error)

    def get_contacts(request):
        try:
            contacts = contact_table.objects.all()
            return contacts
            if contacts:
                return contacts
            return {status: 500, context: "failed to save"}
        except Exception as error:
            return str(error)
