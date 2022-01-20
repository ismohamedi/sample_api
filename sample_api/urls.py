from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from core.api import api as sample_api
from django.conf.urls.static import static
from django.conf import settings


api = NinjaAPI(title="Sample APIs with Django Ninja", docs_url="/docs")
api.add_router("", sample_api)

urlpatterns = [path("admin/", admin.site.urls), path("api/", api.urls)]

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
