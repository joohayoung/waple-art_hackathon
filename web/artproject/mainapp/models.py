from django.db import models
import os
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    name=models.CharField(max_length=50)
    item=models.CharField(max_length=50) # 카테고리 
    public= models.BooleanField(default=False)
    rating= models.IntegerField()
    date=models.DateField(null=True, blank=True)
    image=models.ImageField(upload_to='userimg', null=True)
    comment=models.TextField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        super(Post, self).delete(*args, **kwargs)
        if self.image : 
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
