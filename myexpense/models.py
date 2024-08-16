from django.db import models

# Create your models here.
class Expense(models.Model):
    date=models.CharField(max_length=10,null=False)
    category=models.CharField(max_length=50)
    amount=models.IntegerField()