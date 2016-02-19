import datetime
from django.http import Http404

from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import *
from .views import *

# Create your tests here.

def createNotification():
    u1 = Doctor
    u1.name = "actor"
    testNotification = models.Notification
    testNotification.actor = u1
    testNotification.date = timezone.get_current_timezone()
    testNotification.message = "test"
    testNotification.save()
    return testNotification

class testCreateNotification():
    def createNotificationTest(self):
        Notification = createNotification()
        self.assertEqual("actor",Notification.actor.name)

class ViewsTestCase(TestCase):
    def testIndex(self):
        resp = self.client.get('/Notifications/')
        self.assertEqual(resp.status_code, 200)