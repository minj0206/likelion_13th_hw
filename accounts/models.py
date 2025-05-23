from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.TextField(max_length=3)
    bio = models.TextField(null=True, max_length=30)
