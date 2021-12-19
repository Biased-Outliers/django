from django.db import models

# Create your models here.
class Image(models.Model):
    first_image = models.ImageField()
    second_image = models.ImageField()

    def __str__(self):
        return "I am an image"