"""models for users"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Player(models.Model):
    """proxy model that extense the base data other information"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField(blank=True)
    picture = models.ImageField(upload_to='users/pictures', blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):

        """Return username"""
        return self.user.username

