from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

class userlogin(forms.Form):
    firstname = forms.CharField(label="Enter first name", max_length=50)

    class Meta:
        model = User
        fields = ['username', 'password']




class UserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email","password1", "password2")
       