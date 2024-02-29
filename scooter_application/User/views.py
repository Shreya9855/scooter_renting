from django.http import HttpResponse
from django.shortcuts import render
from .models import User
from .forms import signUpForm

# Create your views here.
def user_signup(request):
    if request.method == "POST":
        form = signUpForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data('name')
            username = form.cleaned_data('username')
            email = form.cleaned_data('email')
            age = form.cleaned_data('age')
            password = form.cleaned_data('password')
            confirm_password = form.cleaned_data('confirm_password')
            address = form.cleaned_data('address')
            form.save()

    return HttpResponse("This is sign up page")
# return render(request,'<url'>,{object})
