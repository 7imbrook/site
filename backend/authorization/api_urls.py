from django.urls import path, re_path
from . import api_view

urlpatterns = [
    re_path("^status/$", api_view.status)
]

