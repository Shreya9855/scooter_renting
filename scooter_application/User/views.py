from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from .forms import signUpForm
from .models import User
# https://pythonguides.com/encrypt-and-decrypt-password-in-django/

def user_signup(request):
    if request.method == "POST":
        form = signUpForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            address = form.cleaned_data['address']           
            if password == confirm_password:
                encrypt_password = make_password(password)
                user_details =  User.objects.create(
                    name=name,
                    username=username,
                    email=email,
                    age=age,
                    password=encrypt_password,
                    confirm_password='########',  # It's better not to store confirm password in the database
                    address=address
                )
                print(user_details)
                print("user created")
                # Redirect to some success page, login page, or homepage
                # return render(request, "success.html", {'user_details': user_details})
            else:
                # Passwords didn't match, add an error message to the form
                form.add_error('confirm_password', "Passwords do not match")
    else:
        form = signUpForm()
    return render(request, "user/sign_up.html", {'form': form})
