from django.db import models

# Create your models here.

class ArtInfoDB(models.Model):
    title = models.CharField(max_length=30)
    host = models.CharField(max_length=30)
    region = models.CharField(max_length=10)
    category = models.CharField(max_length=10)
    start_date = models.DateField(null=True, auto_now=False, auto_now_add=False)
    end_date = models.DateField(null=True, auto_now=False, auto_now_add=False)

    def __str__(self):
        return f'{self.id}: {self.title} - {self.category}'

class PerformanceDB(models.Model):
    artinfo = models.ForeignKey(
        ArtInfoDB, on_delete=models.CASCADE, related_name='performance')
    cl = models.CharField(max_length=10) #소분류
    genre = models.CharField(max_length=10)
    place = models.CharField(max_length=30)
    Vrate = models.CharField(max_length=50, null=True) #관람등급 view rate

class FestivalDB(models.Model):
    artinfo = models.ForeignKey(
        ArtInfoDB, on_delete=models.CASCADE, related_name='festival')
    content = models.TextField() #상세내용

class ArtWorkDB(models.Model):
    artinfo = models.ForeignKey(
        ArtInfoDB, on_delete=models.CASCADE, related_name='artwork')
    cl = models.CharField(max_length=10) #소분류