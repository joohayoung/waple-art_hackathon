from django import forms
from .models import Post

class PostForm(forms.ModelForm): 
    class Meta:
        model = Post
        fields = ('name', 'item', 'public','rating','date','image','comment','country','city')