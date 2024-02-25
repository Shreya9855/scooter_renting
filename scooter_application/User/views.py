from django.http import HttpResponse
from django.shortcuts import render
from .models import User

# Create your views here.
def user_signup(request):
    # return "user has been signed up"
    return HttpResponse("This is sign up page")
# return render(request,'<url'>,{object})

