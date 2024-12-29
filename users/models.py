from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class User(AbstractUser):
    username = models.CharField(max_length=50, blank=False, unique=True)
    email = models.EmailField(unique=True, max_length=255, blank=False)
    password = models.CharField(unique=True, blank=False, max_length=10)
    
    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
# Create your models here.
