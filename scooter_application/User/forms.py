from django import forms

class signUpForm(forms.Form):
    # template_name = 
    name = forms.CharField(max_length= 100)
    username = forms.CharField(max_length= 100)
    email = forms.EmailField()
    age = forms.IntegerField()
    password = forms.PasswordInput()
    confirm_password = forms.PasswordInput()
    address = forms.CharField(widget=forms.Textarea)