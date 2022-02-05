from .models import bloodBankRequest
from django.forms import ModelForm


class bankRequest(ModelForm):
    
    class Meta:
        model = bloodBankRequest
        exclude=('requestID','dateLog')

    
