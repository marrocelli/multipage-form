from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    fname = forms.CharField(label="First Name", max_length=50)
    lname = forms.CharField(label="Last Name", max_length=50)
    username = forms.CharField(label="Username", max_length=50)
    email = forms.EmailField(label="Email")

    class Meta:
        # form will edit a User model
        model = User
        fields = ["fname", "lname", "email", "username", "password1", "password2"]

