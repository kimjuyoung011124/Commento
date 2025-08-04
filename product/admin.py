from django.contrib import admin
from .models import Product, Comment

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'pub_date']
    search_fields = ['title']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content_list', 'content', 'author', 'create_date', 'modify_date']
    list_filter = ['create_date', 'modify_date']
    search_fields = ['author__username']