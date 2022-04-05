from .models import bloodBankRequest
from django.forms import ModelForm
from django import forms
from  location.models import District
from django.core import validators


class bankRequest(ModelForm):
        blood={('A+','A+'),('B+','B+'),('O+','O+'),('AB+','AB+'),('A-','A-'),('O-','O-'),('B-','B-'),('AB-','AB-')}
        first_name=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
        last_name=forms.CharField(max_length=240,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
        gender=forms.ChoiceField(choices=[('Male','Male'),('Female','Female')],widget=forms.RadioSelect)
        email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),required=True)
        mobile=forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone','maxlength':'10','minlength':'10'}),error_messages={'invalid':'invalid mobile number'})
        blood=forms.ChoiceField(choices=blood,widget=forms.Select(attrs={'class': 'form-control',}),)
        address=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}))
        district=forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'District'}),queryset=District.objects.all(),empty_label='Select District')
        city=forms.CharField(widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'City',},))
        class Meta:
            model = bloodBankRequest
            exclude=('requestID','dateLog','userID')
    
