from core.models import Contact
from ninja import ModelSchema

class ContactBase(ModelSchema):
    class Config:
        model = Contact
        model_fields = ['first_name', 'last_name','organisation', 'phone_number']


# schema for contact creaton
class ContactCreate(ContactBase):
    pass


  
class Contact(ModelSchema):
    class Config:
        model = Contact
        model_fields = ['id','first_name', 'last_name','organisation', 'phone_number', 'created_on']
