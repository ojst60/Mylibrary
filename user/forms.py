from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Your email", help_text = "A valid email please")

    class meta:
        model = User
        fields = ['Username', 'email','password1', 'password2' ]
