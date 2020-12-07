from django.urls import path 
from . import views

app_name = 'secondapp'
urlpatterns = [
    path("place_search/", views.place_search, name="place_search"),
    path('place_deatil/<int:pk>', views.place_detail, name="place_detail"),
]