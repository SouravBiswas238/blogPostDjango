from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    slug = models.SlugField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='fallback.png' , blank=True)

    def __str__(self):
        return self.title           # This is the title of the post 