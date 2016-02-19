from django.contrib.auth.models import User
from django.db import models
from Profiles.models import *
import datetime
# Create your models here.

#some global variables
MAX_PRIORITY_INTEGER = 3
MAX_STRING_LENGTH = 500

class Message(models.Model):
    sender = models.CharField(max_length=500, default=None, blank=True, null=True)
    recipients = models.ManyToManyField(User)
    timeSent = models.DateTimeField(auto_now=True)
    text = models.TextField(max_length=None, null=True, blank=True, default=None)
    isRead = models.BooleanField(default=False)

    def __str__(self):
        return "Message: " + self.text



