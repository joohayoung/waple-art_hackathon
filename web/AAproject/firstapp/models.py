from django.db import models

# Create your models here.

class Areainfo(models.Model):
    areaid = models.IntegerField()
    title = models.CharField(max_length = 30)
    genres = models.CharField(max_length = 10)

    def __str__(self):
        return f'{self.id}: 코드 :{self.areaid} / {self.title}'