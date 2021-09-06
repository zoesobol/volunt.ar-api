from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    photo = models.ImageField(null=True, upload_to='users')
    description = models.TextField(null=True)
    dni = models.CharField(max_length=9, unique=True)
    city = models.CharField(max_length=50)
    is_npo = models.BooleanField(null=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True)