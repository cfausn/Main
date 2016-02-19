import datetime
from logs.models import Entry
from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Post

time = timezone.now()
def createPost():
    p = Post
    p.username = "name"
    return p

class ViewsTestCase(TestCase):
    def testIndex(self):
        resp1 = self.client.get('/Register/')
        self.assertEqual(resp1.status_code, 200)

    def testEdit(self):
        resp1 = self.client.get('/Register/edit')
        self.assertEqual(resp1.status_code, 200)

    def testPassword(self):
        resp1 = self.client.get('/Register/password/')
        self.assertEqual(resp1.status_code, 200)
