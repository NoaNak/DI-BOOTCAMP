from django.db import models
from django.contrib.auth.models import User
from films.models import Film, Category, Director

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField()
    favorite_films = models.ManyToManyField(Film)
    favorite_directors = models.ManyToManyField(Director)
    favorite_categories = models.ManyToManyField(Category)

    def __str__(self) -> str:
        return f"User's{self.user} Profile"

