from django.db import models

class Animals(models.Model):
    name = models.CharField(max_length=200)
    animalType = models.CharField(max_length=200)
    breed = models.CharField(max_length=100)
    image = models.ImageField(upload_to='animals/images/')

    def __str__(self):
        return self.name