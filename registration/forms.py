
from django import forms 
from .models import RegisterModel
from location.models import District
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Registration(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),required=True)
    password1 = forms.CharField(help_text='Enter Password',required = True,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),)
    password2 = forms.CharField(required = True,help_text='Enter Password Again',widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),)
    class Meta:
        model=RegisterModel
        fields=['email','password1','password2']
    
   
    