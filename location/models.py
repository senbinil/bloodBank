from django.db import models

# Create your models here.

class District(models.Model):
    name=models.CharField(max_length=50,unique=True,primary_key=True)
    def __str__(self) -> str:
        return self.name
class City(models.Model):
    district=models.ForeignKey("District", on_delete=models.CASCADE)
    name=models.CharField(max_length=50,unique=True)
    def __str__(self) -> str:
        return self.name