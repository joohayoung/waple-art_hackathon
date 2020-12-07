from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class info(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    age=models.IntegerField()
    region=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)