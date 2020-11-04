from django.urls import path 
from . import views

app_name = 'subapp'
urlpatterns = [
    path('test/', views.test, name='test'), #127.0.0.1:8000/subapp/test
    path('search/', views.search, name='search'),
    path('result/', views.result, name='result'),
    path('detail/<int:content_pk>', views.detail, name='detail'),
]