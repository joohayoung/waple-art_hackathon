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
    basic_title = models.ForeignKey(
        ArtInfoDB, on_delete=models.CASCADE, related_name='performance_title')
    basic_host = models.ForeignKey(
        ArtInfoDB, on_delete=models.CASCADE, related_name='performance_host')
    basic_region = models.ForeignKey(
        ArtInfoDB, on_delete=models.CASCADE, related_name='performance_region')
    basic_Sdate = models.ForeignKey(
        ArtInfoDB, on_delete=models.CASCADE, related_name='performance_Sdate')
    basic_Edate = models.ForeignKey(
        ArtInfoDB, on_delete=models.CASCADE, related_name='performance_Edate')
    cl = models.CharField(max_length=10) #소분류
    genre = models.CharField(max_length=10)
    place = models.CharField(max_length=30)
    place = models.CharField(max_length=50) #관람등급 view rate

class FestivalDB(models.Model):
    basic_title = models.ForeignKey(
        ArtInfoDB, on_delete=models.CASCADE, related_name='festival_title')
    basic_host = models.ForeignKey(
        ArtInfoDB, on_delete=models.CASCADE, related_name='festival_host')
    basic_region = models.ForeignKey(
        ArtInfoDB, on_delete=models.CASCADE, related_name='festival_region')
    basic_Sdate = models.ForeignKey(
        ArtInfoDB, on_delete=models.CASCADE, related_name='festival_Sdate')
    basic_Edate = models.ForeignKey(
        ArtInfoDB, on_delete=models.CASCADE, related_name='festival_Edate')
    content = models.TextField() #상세내용

class ArtWorkDB(models.Model):
    basic_title = models.ForeignKey(
        ArtInfoDB, on_delete=models.CASCADE, related_name='artwork_title')
    basic_host = models.ForeignKey(
        ArtInfoDB, on_delete=models.CASCADE, related_name='artwork_host')
    basic_region = models.ForeignKey(
        ArtInfoDB, on_delete=models.CASCADE, related_name='artwork_region')
    basic_Sdate = models.ForeignKey(
        ArtInfoDB, on_delete=models.CASCADE, related_name='artwork_Sdate')
    basic_Edate = models.ForeignKey(
        ArtInfoDB, on_delete=models.CASCADE, related_name='artwork_Edate')
    cl = models.CharField(max_length=10) #소분류