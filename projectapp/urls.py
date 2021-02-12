from django.contrib import admin
from django.urls import path, include
from projectapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('main/', views.main, name = 'main'),
    path('map1/', views.map1, name = 'map1'),
    path('map2/', views.map2, name = 'map2'),
    path('board/', views.board, name = 'board'),

#하영
    path('board_list/', views.board_list, name='board_list'),
    path('board_view//<int:board_id>/', views.board_view, name='board_view'),
    path('board_write/', views.board_write, name='board_write'),
    path('board_edit/', views.board_edit, name='board_edit'),
    path('post/', views.post, name='post'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)