from django.db import models
# from subapp.models import ArtInfoDB
# Create your models here.

class PlaceDB(models.Model):
    #현지 외지인 합치기 ** 전체 수 현지인 총합 + 외지인총합 + 외국인총합
    title = models.CharField(max_length=10) #장소명
    address = models.TextField() #주소
    region = models.CharField(max_length=10)#행정구역
    image_url = models.TextField(null=True)
    allsum = models.IntegerField() #전체 유동인구

    kids_m = models.IntegerField() #남자 10대미만
    ten_m = models.IntegerField()
    twenty_m = models.IntegerField()
    thirty_m = models.IntegerField()
    forty_m = models.IntegerField()
    fifty_m = models.IntegerField() 
    old_m = models.IntegerField() #남자 60대이상

    kids_w = models.IntegerField() #여자 10대미만
    ten_w = models.IntegerField()
    twenty_w = models.IntegerField()
    thirty_w = models.IntegerField()
    forty_w = models.IntegerField()
    fifty_w = models.IntegerField() 
    old_w = models.IntegerField() #여자 60대이상

    def __str__(self):
        return f'{self.id}: {self.title} - {self.region} - {self.allsum}'