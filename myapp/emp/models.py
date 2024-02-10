from django.db import models

# Create your models here.

class Emp(models.Model):
    name=models.CharField(max_length=200)
    emp_id=models.CharField(max_length=10)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=200)
    department=models.CharField(max_length=10)
    working=models.BooleanField(default=True)
    

    #def __str__(self):
     #  return self.name
