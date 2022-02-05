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
    pincode=models.IntegerField()
    city=models.CharField(max_length=300)
    district=models.CharField(max_length=300)
    mobile=models.CharField(max_length=10)
    dateLog=models.DateTimeField(auto_now_add=True)
    blood=models.CharField(max_length=4)
    checkme=models.BooleanField(default=False)
    