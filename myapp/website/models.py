from django.db import models

# Create your models here.

class student(models.Model):  #Model is parent class so that student can inherit inherit from Model and create database tables
    name=models.CharField(max_length=200)
    college=models.CharField(max_length=200)
    age=models.IntegerField(max_length=10)
    is_active=models.BooleanField(default=False)
    
