from django.db import models
from subapp.models import ArtInfoDB
# Create your models here.

class Gender(models.Model):
    title = models.ForeignKey(
        ArtInfoDB, on_delete=models.CASCADE, related_name='gender_title')
    male= models.IntegerField()
    female= models.IntegerField()
    
class Age(models.Model):
    title = models.ForeignKey(
        ArtInfoDB, on_delete=models.CASCADE, related_name='age_title')
    Teens= models.IntegerField()
    Twenties= models.IntegerField()
    Thirties= models.IntegerField()
    Forty= models.IntegerField()
    Fifties= models.IntegerField()
    Sixteen= models.IntegerField()