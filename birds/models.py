from django.db import models

# Create your models here.
class BirdPhoto(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='birds/photos/')
    #photo = models.ImageField(upload_to='birds/photos/', null=True, blank=True)

    def __str__(self):
        return self.name
