from django.contrib.auth.hashers import make_password,check_password
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from .forms import logInForm, signUpForm
from .models import User
# https://pythonguides.com/encrypt-and-decrypt-password-in-django/

def user_signup(request):
    if request.user.is_authenticated:
        return redirect('/')

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
                return render(request, "login.html", {'user_details': user_details})
            else:
                # Passwords didn't match, add an error message to the form
                form.add_error('confirm_password', "Passwords do not match")
    else:
        form = signUpForm()
    return render(request, "sign_up.html", {'form': form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == "POST":
        form = logInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user_authenticate = authenticate(request,username=username,password = password)
            print(f'user_authenticate: {user_authenticate}')
            if user_authenticate is not None:
                print('logged in')
                print(login(request, user_authenticate, backend=None))
                return redirect('/')
            else:
                form.add_error(None, "Authentication failed")
        return render(request, "login.html")
    else:
        form = logInForm()  
        
    return render(request, "login.html", {'form': form})

def user_logout(request):
    logout(request)
    return redirect('/')
