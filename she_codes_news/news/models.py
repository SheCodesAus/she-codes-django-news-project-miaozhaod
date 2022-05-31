from django.db import models


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    content = models.TextField()
    img = models.CharField(max_length=500, default='https://picsum.photos/600')
