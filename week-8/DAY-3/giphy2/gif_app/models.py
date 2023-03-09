from django.db import models

# Category(parent) <- Gif(child) 

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Gif(models.Model):
    author = models.CharField(max_length=50)
    uploader_name = models.CharField(max_length=50)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name='gifs')
    
    def __str__(self):
        return self.author
