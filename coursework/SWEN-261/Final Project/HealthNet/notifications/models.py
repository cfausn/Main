from django.db import models
from django.contrib.auth.models import User

MAX_STRING_LENGTH = 500 #Max length for any string not listed specifically here

class MakeNotification(models.Manager):
    def new_entry(self,actor,message,now,url,priority,read):

        i = 0

        for n in Notification.objects.all():
            i += 1


        return self.create(actor=actor, message=message, date=now, url=url, priority=priority, read=read, theID=i)

class Notification(models.Model):
    actor = models.ForeignKey(User)
    message = models.CharField(max_length=MAX_STRING_LENGTH)
    date = models.DateTimeField()
    url = models.URLField()
    priority = models.IntegerField(default=0) #Value from 0 - 2 depending on severity
    read = models.BooleanField(default=False)
    theID = models.IntegerField(default=0)
    objects = MakeNotification()
    class Meta:
        verbose_name = 'Notification'

    def __str__(self):
        return self.actor.username