from django.shortcuts import render
from .models import Product

def content_list(request):
    products = Product.objects.all()
    context = {'products': products}  # 여기 이름을 content_list로 맞춤
    return render(request, 'product/content_list.html', context)