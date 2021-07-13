from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User


class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    GenderChoices = [("Male", "Male"), ("Female", "Female")]
    name = models.CharField(max_length=10)
    id = models.CharField(max_length=20,primary_key=True)
    address = models.CharField(max_length=30)
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=GenderChoices)
    country = CountryField()
#    Branch = models.ForeignKey(Car, on_delete=models.CASCADE, default=None)

# Create your models here.
