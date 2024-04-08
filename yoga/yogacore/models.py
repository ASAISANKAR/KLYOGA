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

class Profile(models.Model):
    username=models.CharField(max_length=100)
    name = models.CharField(default="core",max_length=100)
    email=models.EmailField(default="core@gmail.com")
    phonenumber=models.CharField(default="9XXXXXXXX",max_length=10)
    idnumber=models.CharField(default="22000XXXXX",max_length=10)
    image=models.CharField(default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8pqpC6IgkvdxOH-qCcentLTmv_U4TeAVMPutepRWn9w&s",max_length=500)
    branch=models.CharField(default="CSE",max_length=10)
    college=models.CharField(default="KLU",max_length=10)

    class Meta:
        db_table="Profile"
