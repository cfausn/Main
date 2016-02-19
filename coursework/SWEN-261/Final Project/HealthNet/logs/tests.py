from django.test import TestCase

from .models import models, Entry, MakeEntry
from Profiles import *


# Create your tests here.

def createEntry():
    c = Entry.objects.create(actor = "actor")
    return c


class TestCreateEntry(TestCase):
    def TestCreateEntry(self):
        c = createEntry()
        self.assertEquals("actor", c.actor)