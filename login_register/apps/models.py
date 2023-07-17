from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    website = models.CharField(max_length=200, null=True)
    street = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    follow = models.CharField(max_length=200, null=True, blank=True)
    followers = models.CharField(max_length=200, null=True, blank=True)
    views = models.IntegerField(default=0)
    job = models.CharField(max_length=200, null=True, blank=True)
    hobbies = models.CharField(max_length=200, null=True, blank=True)



