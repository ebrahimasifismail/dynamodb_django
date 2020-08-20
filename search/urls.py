from django.urls import path, include
from . import views



urlpatterns = [
    # path("", include("rest_auth.urls")),
    path("search/", views.search, name="search"),
    
]