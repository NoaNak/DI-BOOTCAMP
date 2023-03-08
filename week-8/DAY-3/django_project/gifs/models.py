from django.db import models

# Create your models here.

class Gifs(models.Model):

    author = models.CharField(max_length=50)
    uploader_name = models.CharField(max_length=50)
    url = models.URLField(max_length=50)   
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author 

class Category(models.Model):
    name = models.CharField(max_length=50)
    gifs = models.ManyToManyField(Gifs, related_name='categories')

    def __str__(self):
        return self.name 
    

    
    