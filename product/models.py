from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title