from django.db import models

# Create your models here.

class Post(models.Model):

    author = models.CharField(max_length=50) # varchar c sur sql et charfield sur django
    title = models.CharField(max_length=50) 
    body = models.TextField()