from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name = 'main'),
    path('map1/', views.map1, name = 'map1'),
    path('map2/', views.map2, name = 'map2'),
    path('map2_1/', views.map2_1, name='map2_1'),
    path('board/', views.board, name = 'board'),
]