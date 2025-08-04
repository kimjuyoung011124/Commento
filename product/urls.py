from django.urls import path
from . import views

app_name = 'product'   # 네임스페이스를 사용할 경우 추가해 주세요

urlpatterns = [
    # 1) 게시글 목록 페이지 (예: /product/)
    path('', views.content_list, name='content_list'),

    # 2) 게시글 상세 페이지 (예: /product/1/)
    path('<int:content_id>/', views.detail, name='detail'),

    # 3) 댓글 생성 요청 (예: /product/comment/create/1/)
    path('comment/create/<int:content_id>/',
         views.comment_create,
         name='comment_create'),

    # 4) 댓글 수정 요청 (예: /product/comment/update/5/)
    path('comment/update/<int:comment_id>/',
         views.comment_update,
         name='comment_update'),

    # 5) 댓글 삭제 요청 (예: /product/comment/delete/5/)
    path('comment/delete/<int:comment_id>/',
         views.comment_delete,
         name='comment_delete'),
]