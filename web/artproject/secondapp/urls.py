from django.urls import path 
from . import views

app_name = 'secondapp'
urlpatterns = [
    path('search_place/', views.search_place, name='search_place'),
    path('result/', views.result, name='result'),
]