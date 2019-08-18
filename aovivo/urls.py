from django.urls import path
from aovivo.views import aovivo

urlpatterns = [
    path('ao-vivo/<slug:slug>', aovivo),
]