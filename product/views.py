from django.shortcuts import render, get_object_or_404
from .models import Product

# 목록 페이지
def content_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product/content_list.html', context)

# 상세 페이지
def detail(request, content_id):
    product = get_object_or_404(Product, pk=content_id)
    context = {'content_list': product}
    return render(request, 'product/content_detail.html', context)