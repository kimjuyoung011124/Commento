from django.urls import path
from . import views

urlpatterns = [
    path('', views.content_list, name='product_list'),
    path('<int:content_id>/', views.detail, name='detail'),
]