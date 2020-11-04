from django.db import models

# Create your models here.
class Post(models.Model):
    name=models.CharField(max_length=50)
    item=models.CharField(max_length=50) # 카테고리 
    public= models.BooleanField(default=False)
    rating= models.IntegerField()
    date=models.DateField(null=True, blank=True)
    image=models.ImageField()
    comment=models.TextField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name