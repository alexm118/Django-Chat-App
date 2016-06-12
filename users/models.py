from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, models.SET_NULL, null=True)
    bio = models.TextField('User Bio', blank=True, null=True)
    gravatar_email = models.EmailField('Gravatr Email')
