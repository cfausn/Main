from django.shortcuts import render
from .forms import MessageForm
from logs.models import Entry
import datetime
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import Http404

from .models import Message
from Profiles.models import *
from notifications.models import Notification

def createMessage(request):
    guser = None
    theId = request.user.id

    for user in User.objects.all():
        if user.id == int(theId):
            guser = user

    if guser==None:
        raise Http404("User not found")

    isPatient = userIsPatient(guser)
    isDoctor = userIsDoctor(guser)
    isNurse = userIsNurse(guser)
    isAdmin = userIsAdmin(guser)

    n = []

    for notification in Notification.objects.all():
        if str(notification) == request.user.username:
            if notification.read == False:
                n.append(notification)

    if request.method == "POST":
        s = MessageForm(request.POST)

        if s.is_valid():
            s.save()
            Entry.objects.new_entry(request.user, 'New Message', datetime.datetime.now())
            return render(request, 'Messages/index.html')
        return render(request, 'Messages/index.html')
    else:
        s = MessageForm(guser)
        return render(request,'Messages/createMessage.html', {
            'firstName': request.user.first_name,
            'lastName': request.user.last_name,
            'id' : theId,
            'isAdmin': isAdmin,
            'isPatient': isPatient,
            'isDoctor': isDoctor,
            'isNurse': isNurse,
            'notifications' : n,
            'notifyLength' : len(n),
            'form': s,
        })

@login_required
def messages(request):
    guser = None
    theId = request.user.id

    for user in User.objects.all():
        if user.id == int(theId):
            guser = user

    if guser==None:
        raise Http404("User not found")

    isPatient = userIsPatient(guser)
    isDoctor = userIsDoctor(guser)
    isNurse = userIsNurse(guser)
    isAdmin = userIsAdmin(guser)

    n = []

    for notification in Notification.objects.all():
        if str(notification) == request.user.username:
            if notification.read == False:
                n.append(notification)

    user = request.user
    messages = user.message_set.all()
    return render(request, 'Messages/messages.html', {
        'firstName': request.user.first_name,
        'lastName': request.user.last_name,
        'id' : theId,
        'isAdmin': isAdmin,
        'isPatient': isPatient,
        'isDoctor': isDoctor,
        'isNurse': isNurse,
        'messages': messages,
        'notifications' : n,
        'notifyLength' : len(n),
    })

# Create your views here.
