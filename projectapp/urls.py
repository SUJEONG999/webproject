from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name = 'main'),
    path('map1/', views.map1, name = 'map1'),
    path('map2/', views.map2, name = 'map2'),
    path('board/', views.board, name = 'board'),

#하영
    path('board_list/', views.board_list, name='board_list'),
    path('board_view/', views.board_view, name='board_view'),
    path('board_write/', views.board_write, name='board_write'),
    path('board_edit/', views.board_edit, name='board_edit'),
]

#     path('download/<int:pk>', views.board_download_view, name="board_download"),
#    # 페이징 처리 / url 추가
#     path('', views.BoardListView.as_view(), name='board_list'),
#     # 게시글 검색기능 구현
#     path('search/', views.SearchFormView.as_view(), name='search'),