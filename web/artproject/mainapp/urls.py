from django.urls import path 
from . import views

from django.conf.urls.static import static
from django.conf import settings

app_name = 'mainapp'
urlpatterns = [
    path('', views.home, name='home'), 
    path('map/', views.map, name='map'), #postlist보여줌
    path('<int:pk>/',views.posting, name="posting"), #post 세부내용
    path('upload/', views.upload, name='upload'), #postupload 
    path('<int:pk>/remove/', views.remove_post, name='remove_post'),
]

# 이미지 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)