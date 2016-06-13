from __future__ import unicode_literals

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Room(models.Model):
    name = models.CharField('Room Name', max_length=255)
    label = models.SlugField(unique=True)
    memebers = models.ManyToManyField(User)

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages')
    handle = models.ForeignKey(User, models.SET_NULL, null=True, related_name='message_handle')
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)
