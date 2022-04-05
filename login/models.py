from datetime import datetime
from tkinter import CASCADE
from django.db import models
from registration.models import RegisterModel
# Create your models here.

def getrequestID():
    date=datetime.now()
    return 'KBBP'+date.strftime('%f')+date.strftime('%d')

class bloodBankRequest(models.Model):
    requestID=models.CharField(max_length=300,primary_key=True,default=getrequestID)
    city=models.CharField(max_length=300)
    district=models.CharField(max_length=300)
    mobile=models.CharField(max_length=10)
    dateLog=models.DateTimeField(auto_now_add=True)
    blood=models.CharField(max_length=4)
    checkme=models.BooleanField(default=False)
    first_name=models.CharField(max_length=20,default='')
    last_name=models.CharField(max_length=100,default='')
    gender=models.CharField(max_length=20,default='')
    email=models.EmailField(null=False,default='')
    address=models.CharField(max_length=200,default='')
    
    