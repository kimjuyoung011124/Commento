from django.contrib import admin
from django.urls import path, include  # include 추가

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('product/', include('product.urls')),  # ✅ product 앱 경로 연결
]