from django.db import models

# Create your models here.

class Feedba(models.Model):
    name=models.CharField(max_length=100)
    iid=models.CharField(max_length=100)
    email=models.EmailField()
    gende = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    gender = models.CharField(max_length=20, choices=gende)
    phonenumber=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    Comments=models.CharField(max_length=100,null=True)
    class Meta:
        db_table="Feedback" #To show the table name to the user

class Feed(models.Model):
    name=models.CharField(max_length=100)
    iid=models.CharField(max_length=100)
    email=models.EmailField()
    gende = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    gender = models.CharField(max_length=20, choices=gende)
    phonenumber=models.CharField(max_length=100)
    branch=models.CharField(max_length=100,null=True)
    Comments=models.CharField(max_length=100,null=True)
    date=models.DateField()
    class Meta:
        db_table="Feed" #To show the table name to the user




