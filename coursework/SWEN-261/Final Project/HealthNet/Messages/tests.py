from django.test import TestCase
from django.core.urlresolvers import reverse

from Messages.models import Message
from Profiles.models import *


def testCase1():
    u1 = Nurse
    u1.name = u1
    u2 = Doctor
    u2.name = u2
    text = "foo"
    message1 = Message
    message1.sender = u1
    message1.recipient = u2
    message1.text = text

class ViewsTestCase(TestCase):
    def testIndex(self):
        resp = self.client.get('/Messages/')
        self.assertEqual(resp.status_code, 302)

    def testCreateMessage(self):
        resp = self.client.get('/Messages/createMessage.html')
        self.assertEqual(resp.status_code, 200)

    def testMessages(self):
        resp = self.client.get('/Messages/messages.html')
        self.assertEqual(resp.status_code, 200)
