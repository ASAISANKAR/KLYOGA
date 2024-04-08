from django.db import models
class Signup(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    class Meta:
        db_table = "Signup"

class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    date=models.DateField()
    class Meta:
        db_table = "Login"