from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name = 'main'),
    path('map1/', views.map1, name = 'map1'),
    path('map2/', views.map2, name = 'map2'),
    path('board/', views.board, name = 'board'),
    path('exam23/', views.exam23, name = 'exam23'),
    path('exam22/', views.exam22, name = 'exam22'),
]