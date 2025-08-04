from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.utils import timezone

from .models import Product, Comment
from .form import CommentForm


# 1) 게시글 목록 페이지
def content_list(request):
    products = Product.objects.all()
    return render(request, 'product/content_list.html', {
        'products': products
    })


# 2) 게시글 상세 페이지
def detail(request, content_id):
    product = get_object_or_404(Product, pk=content_id)
    form = CommentForm()
    return render(request, 'product/content_detail.html', {
        'content_list': product,
        'form': form,
    })


# 3) 댓글 생성 처리
@login_required(login_url='accounts:login')
def comment_create(request, content_id):
    product = get_object_or_404(Product, pk=content_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.content_list = product
            comment.author = request.user
            comment.save()
            return redirect('product:detail', content_id=product.id)
    else:
        form = CommentForm()

    return render(request, 'product/content_detail.html', {
        'content_list': product,
        'form': form,
    })


# 4) 댓글 수정 처리
@login_required(login_url='accounts:login')
def comment_update(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    # 작성자만 수정 가능
    if request.user != comment.author:
        raise PermissionDenied

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('product:detail', content_id=comment.content_list.id)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'product/comment_form.html', {
        'form': form,
        'comment': comment,
    })


# 5) 댓글 삭제 처리
@login_required(login_url='accounts:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    # 작성자만 삭제 가능
    if request.user != comment.author:
        raise PermissionDenied

    product_id = comment.content_list.id
    comment.delete()
    return redirect('product:detail', content_id=product_id)