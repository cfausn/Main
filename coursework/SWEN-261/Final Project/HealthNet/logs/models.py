from django.db import models
from django.contrib.auth.models import User

MAX_STRING_LENGTH = 500 #Max length for any string not listed specifically here

class MakeEntry(models.Manager):
    def new_entry(self,actor,message,now):
        return self.create(actor=actor, message=message, date=now)

class Entry(models.Model):
    actor = models.ForeignKey(User)
    message = models.CharField(max_length=MAX_STRING_LENGTH)
    date = models.DateTimeField()
    objects = MakeEntry()
    class Meta:
        verbose_name = 'Entry'

    def __str__(self):
        return self.actor.username

