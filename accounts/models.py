from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField

class CustomUser(AbstractUser):
    birthdate = models.DateField(null=True, blank=True)
    country = CountryField(blank=True)  # Use CountryField from django-countries
    interests = models.ManyToManyField('Interest', blank=True)

class Interest(models.Model):
    INTEREST_CHOICES = [
        ('coding', 'Coding'),
        ('reading', 'Reading'),
        ('gaming', 'Gaming'),
        ('hiking', 'Hiking'),
        # Add other interests as needed
    ]
    name = models.CharField(max_length=50, choices=INTEREST_CHOICES)

    def __str__(self):
        return self.name
