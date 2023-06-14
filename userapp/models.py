from django.db import models
from django.contrib.auth.models import User
class Account(models.Model):
    tanlov = [
        ("Erkak", "Erkak"),
        ("Ayol", "Ayol"),
    ]
    jins = models.CharField(max_length=10, choices=tanlov)
    shahar = models.CharField(max_length=100)
    davlat = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.jins


# Create your models here.
