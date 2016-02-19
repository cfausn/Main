from django.shortcuts import render
from django.views import generic

from django.http import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from logs.models import Entry
import datetime
from Register.forms import get_hospitals, PatientForm
from django import forms


from django.contrib import messages


# Create your views here.

def user_login(request):
    logout(request)
    context = RequestContext(request)

    s = PatientForm()
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        user = authenticate(username=username, password=password)


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

def user_redirect(request):
    return render_to_response('Login/redirect.html', context=RequestContext(request))
