from django.urls import include,path
from . import views

urlpatterns = [
    path("register", views.register_scooter, name='register'),
    path("rent", views.scooter_rent, name='rent')
]
