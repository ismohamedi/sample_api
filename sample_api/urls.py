from typing import List
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from core.views import *
from core.schema import *


api = NinjaAPI(title="Sample APIs", docs_url="/docs")


@api.get("/add", response=Contact, tags="Create Contact")
def add(request, contact: ContactCreate):
    return create_contact(contact)

@api.get("/get-contact", response=List[Contact], tags="Get Contacts")
def get_contact(request):
    return get_contacts(request)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]