from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(null=True, blank=True, upload_to="static/uploads/")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField()

    def __str__(self):
        return self.title
