from django.db import models

# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    memo = models.CharField(max_length=50)
    gender = models.BooleanField()
    age = models.IntegerField()
    createdate = models.DateField()