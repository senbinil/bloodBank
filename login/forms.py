from re import A
from .models import bloodBankRequest
from django.forms import ModelForm
from django import forms

class bankRequest(ModelForm):

    class Meta:
        model = bloodBankRequest
        blood={('A+','A+'),('B+','B+'),('O+','O+'),('AB+','AB+'),('A-','A-'),('O-','O-'),('B-','B-'),('AB-','AB-')}
        exclude=('requestID','dateLog','userID')
        widgets={
            'pincode':forms.TextInput(attrs={'class':'form-control text-center','placeholder':'Pincode'}),
            'city':forms.TextInput(attrs={'class':'form-control text-center','placeholder':'City'}),
            'district':forms.TextInput(attrs={'class':'form-control text-center','placeholder':'District'}),
            'mobile':forms.TextInput(attrs={'class':'form-control text-center','placeholder':'Mobile','type':'text'}),
            'blood':forms.Select(attrs={'class':'form-control text-center','placeholder':'Pincode'}, choices=blood),
        }
    
