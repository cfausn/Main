from django.shortcuts import *
from Register.forms import get_hospitals, PatientForm
from django.contrib.auth import authenticate, login, logout
from Profiles.models import userIsAdmin, userIsDoctor, userIsNurse, userIsPatient
from notifications.models import *

from logs.models import Entry
from django.contrib import messages
import datetime




def indexView(request):

    if request.method == "POST":

        try:
            if request.POST['login']:
                logout(request)
                context = RequestContext(request)

                if request.method == 'POST':
                    username = request.POST['username'].lower()
                    password = request.POST['password']

                    user = authenticate(username=username, password=password)
                    s = PatientForm()


                    if user:
                        if user.is_active:
                            login(request, user)
                            Entry.objects.new_entry(user, 'User: %s, login attempt' % str(user), datetime.datetime.now())

                            return render_to_response('Login/redirect.html', context=RequestContext(request,{'username' : user.username,}))
                        else:
                            # An inactive account was used - no logging in!

                            messages.warning(request, "Your account is disabled. Please contact an administrator to reactivate your account.")
                            return render(request, 'HealthNet/index.html',context={'user':s})
                    else:
                        messages.warning(request, "Invalid login credentials")
                        return render(request, 'HealthNet/index.html', context={'user':s})

                else:
                    # No context variables to pass to the template system, hence the
                    # blank dictionary object...
                    return render_to_response('HealthNet/index.html', {}, context)

        except:
            s = PatientForm(request.POST)

            if s.is_valid():
                s.save()
                user = authenticate(username=(request.POST['username']).lower(),
                                    password=request.POST['password1'])
                login(request,user)
                return render(request, 'Register/posted.html')
    else:
        s = PatientForm()
    return render(request,'HealthNet/index.html', {
        'user': s
    })



def custom404Page(request):
    targetUsername = request.user
    theId = targetUsername.id
    isPatient = userIsPatient(request.user)
    isDoctor = userIsDoctor(request.user)
    isNurse = userIsNurse(request.user)
    isAdmin = userIsAdmin(request.user)
    access = userIsAdmin(request.user)

    n = []

    for notification in Notification.objects.all():
        if str(notification) == targetUsername.username:
            n.append(notification)

    return render(request, 'HealthNet/404page.html', {
                'username' : targetUsername,
                'isPatient' : isPatient,
                'isDoctor' : isDoctor,
                'isNurse' : isNurse,
                'isAdmin' : isAdmin,
                'id' : theId,
                'notifications' : n,
                'notifyLength' : len(n),
            })




"""
    hospitals = get_hospitals()
    return render(request,'HealthNet/index.html', {'hospitals':hospitals})"""