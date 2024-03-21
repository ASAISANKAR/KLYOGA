from django.db import models

# Create your models here.
class Feedback(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    Comments=models.CharField(max_length=100)
    class Meta:
        db_table="Feedback" #To show the table name to the user