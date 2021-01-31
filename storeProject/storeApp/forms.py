from .models import userInfo,User,genre,book,cart
from django import forms
from django.contrib.auth.forms import UserCreationForm

class userForm(UserCreationForm):
    class Meta:
        model = userInfo
        fields = ['username','first_name','last_name','age','gender','contact','email']

class Login_form(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(widget =forms.PasswordInput)     


    