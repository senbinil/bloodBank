from tkinter import CASCADE
from django.db import models
from registration.models import RegisterModel
# Create your models here.

class bloodBankRequest(models.Model):
    requestID=models.CharField(max_length=300,primary_key=True)
    userID=models.ForeignKey(RegisterModel,on_delete=models.CASCADE)
    pincode=models.IntegerField()
    city=models.CharField(max_length=300)
    district=models.CharField(max_length=300)
    mobile=models.CharField(max_length=10)
    dateLog=models.DateTimeField(auto_created=True)
    blood=models.CharField(max_length=4)

    