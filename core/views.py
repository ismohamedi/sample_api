from django.shortcuts import render
from .models import *

# Create your views here.

class Contact:
    def __init__(self):
        pass

    def create_contact(request,contact):
        try:
            contact = Contact.objects.create(**contyact)
            contact.save()
            if contact:
                return contact
            return {error: 'failed to save'}
        except Exception as error:
            return str(error)
    
    def get_contact(request):
        try:
            contacts = Contact.objects.all()
            return contacts
            if contact:
                return contact
            return {status: 500, context: 'failed to save'}
        except Exception as error:
            return str(error)



