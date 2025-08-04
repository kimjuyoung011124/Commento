from django.db import models
from django.contrib.auth.models import User

# 제품(또는 게시글) 모델
class Product(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title

# 댓글 모델
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content_list = models.ForeignKey(Product, on_delete=models.CASCADE)  # Product와 연결
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.content[:20]  # 댓글 앞 20글자만 표시