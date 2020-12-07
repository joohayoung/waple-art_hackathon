from django.urls import path 
from . import views

app_name = 'subapp'
urlpatterns = [
    path('search/', views.search, name='search'),
    path('detail/<int:content_pk>', views.detail, name='detail'),
]