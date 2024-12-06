from django.db import models

class Users(models.Model):
    email = models.CharField(max_length = 40,blank=False,default='')
    password = models.CharField(max_length=40,blank=False,default='')
# Create your models here.
