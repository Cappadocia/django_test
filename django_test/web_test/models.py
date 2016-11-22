from django.db import models
from django.db.models.fields.related import OneToOneField

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
    
    
class Group(models.Model):
    name = models.CharField(max_length=50)
    
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    #建立Group和User表多对多的关系
    group_relation = models.ManyToManyField('Group')
    #一对一表关系OneToOneField