from django.contrib.auth import get_user_model
from django.db import models


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200), 
    # on_delete means if you delete a user, it means everything associated with that user will be deleted
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    content = models.TextField()
    image_url = models.CharField(max_length=500, default="https://picsum.photos/600")
