from django.db import models

# Create your models here.

class User(models.Model):
    username = models.TextField(max_length=20)
    profile_pic = models.ImageField(upload_to='profile_image')

