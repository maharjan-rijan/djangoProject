from django.db import models
class News (models.Model):
    news_title = models.CharField(max_length=100)
    news_description = models.TextField()
# Create your models here.
