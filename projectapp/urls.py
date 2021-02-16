from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name='main'),
    path('map1/', views.map1, name='map1'),
    path('map2/', views.map2, name='map2'),
    path('map2_1/', views.map2_1, name='map2_1'),
    path('board/', views.board, name='board'),
    path('register/', views.register, name='register'),  # 수정's 추가
    path('login/', views.login, name='login'),  # 수정's 추가
    path('logout/', views.logout, name='logout'),  # 수정's 추가
    path('board/<int:pk>/', views.board_view, name='board_view'),
    path('board_write/', views.board_write, name='board_write'),
    path('write/', views.write, name='write'),
    path('board/<int:pk>/remove/', views.remove_board, name='board_remove'),
    path('board/update/<int:pk>', views.update_board, name='board_update'),
    path('board_search/', views.search, name='search'),


    # path("search1/<writer>", views.search1, name="search1"),
    # path("search2/<contents>", views.search2, name="search2"),
    # path('search1', views.search1, name='search1'),
]

# 이미지 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
