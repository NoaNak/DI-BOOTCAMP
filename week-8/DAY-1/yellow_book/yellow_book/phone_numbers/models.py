from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


