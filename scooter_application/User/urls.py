from django.urls import include,path
from . import views

urlpatterns = [
    path("signup", views.user_signup)
]
