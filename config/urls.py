from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    # ↓ 네임스페이스 지정
    path('product/', include(('product.urls', 'product'), namespace='product')),
    path('accounts/', include('accounts.urls')),
]