from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=60)
    published_at=models.DateTimeField()
    description=models.TextField()
    author_name=models.CharField(max_length=20)

    def __str__(self):
        return self.published_at



class Comment(models.Model):
    post=models.ForeignKey(Post)
    description=models.TextField()
    published_at=models.DateTimeField(default=timezone.now())


