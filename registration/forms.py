
from django import forms 
from .models import RegisterModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Registration(UserCreationForm):
    blood={('A+','A+'),('B+','B+'),('O+','O+'),('AB+','AB+'),('A-','A-'),('O-','O-'),('B-','B-'),('AB-','AB-')}
    first_name=forms.CharField(max_length=200,required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),)
    last_name=forms.CharField(max_length=240,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),)
    dob=forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date Of Birth','type':'date'}),)
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),)
    password1 = forms.CharField(help_text='Enter Password',required = True,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),)
    password2 = forms.CharField(required = True,help_text='Enter Password Again',widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),)
    gender=forms.ChoiceField(choices=[('Male','Male'),('Female','Female')],widget=forms.RadioSelect)
    pincode=forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Pincode','type':'text'}),)
    district=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'District'}),)
    city=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),)
    blood=forms.ChoiceField(choices=blood,widget=forms.Select(attrs={'class': 'form-control',}),)
    phone=forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),)
    class Meta:
        model=RegisterModel
        fields=['first_name','last_name','dob','email','password1','password2','pincode','district','phone','city','gender','blood']
    
   
    