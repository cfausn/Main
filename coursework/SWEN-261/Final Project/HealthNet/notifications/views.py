from django.shortcuts import render, redirect
from django.template import *
from django.http import HttpResponseNotFound
from notifications.models import Notification
from logs.models import Entry


# Create your views here.
def index(request):

    i = request.POST['id']

    for n in Notification.objects.all():

        if n.theID == int(i):
            n.read = True
            n.save()

    return redirect(request.META['HTTP_REFERER'])