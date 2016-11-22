from django.db import models

# Create your models here.

class UserType(models.Model):
    name = models.CharField(max_length=50)

class UserInfo(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    memo = models.TextField(default = 'xxxx')
    gender = models.BooleanField(default = False)
    Age = models.IntegerField(default = 19)
    createdate = models.DateField(default = '2016-11-23')
    typeId = models.ForeignKey(UserType)