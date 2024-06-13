from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    article = models.TextField()
    created_by = models.CharField(max_length=100)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
