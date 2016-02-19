from django.shortcuts import render, get_object_or_404, redirect
from .forms import *

from Profiles.models import *
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from logs.models import Entry
from notifications.models import Notification

from django.contrib.auth.models import User




# Create your views here.

def index(request):
    if request.method == "POST":
        s = PatientForm(request.POST)

        if s.is_valid():
            s.save()
            user = authenticate(username=request.POST['username'],
                                password=request.POST['password1'])
            login(request,user)
            return render(request, 'Register/posted.html')
    else:
        s = PatientForm()
    return render(request,'Register/form.html', {
        'user': s
    })

def edit(request, theId):
    user = None
    for guser in User.objects.all():
        if guser.id == int(theId):
            user = guser


    isPatient = userIsPatient(user)
    isDoctor = userIsDoctor(user)
    isNurse = userIsNurse(user)
    isAdmin = userIsAdmin(user)
    patient = None
    for patientIt in Patient.objects.all():
        if patientIt.theUser == user:
            patient = patientIt

    nn = []
    for notification in Notification.objects.all():
        if str(notification) == request.user.username:
            if notification.read == False:
                nn.append(notification)

    for guser in User.objects.all():
        if guser.id == int(theId):
            user = guser

    if user==None:
        raise Http404("User not found")

    if request.method == "POST":
        if isPatient:
            s = EditPatientForm(request.POST, instance=user)
            if s.is_valid():
                s.save()

                return render(request, 'Register/editposted.html')

        elif isDoctor:
            s = EditDoctorForm(request.POST, instance=user)
            if s.is_valid():
                s.save()

                return render(request, 'Register/editposted.html')

        elif isNurse:
            s = EditDoctorForm(request.POST, instance=user)
            if s.is_valid():
                s.save()

                return render(request, 'Register/editposted.html')

        elif isAdmin:
            s = EditAdminForm(request.POST, instance=user)
            if s.is_valid():
                s.save()

                return render(request, 'Register/editposted.html')
    else:
        user = None
        for guser in User.objects.all():
            if guser.id == int(theId):
                user = guser
        isPatient = userIsPatient(user)
        isDoctor = userIsDoctor(user)
        isNurse = userIsNurse(user)
        isAdmin = userIsAdmin(user)
        patient = None
        for patientIt in Patient.objects.all():
            if patientIt.theUser == user:
                patient = patientIt

        for patientIt in Doctor.objects.all():
            if patientIt.theUser == user:
                patient = patientIt
        nn = []
        for notification in Notification.objects.all():
            if str(notification) == request.user.username:
                if notification.read == False:
                    nn.append(notification)

        if isPatient:
            s = EditPatientForm(initial={
                'email': user.email,
                'firstName': user.first_name,
                'middleName': patient.middleName,
                'lastName': user.last_name,
                'suffix': patient.suffix,
                'phoneNumber': patient.phoneNumber,
                'dateOfBirth': patient.dateOfBirth,
                'addressLine1': patient.addressLine1,
                'addressLine2': patient.addressLine2,
                'city': patient.city,
                'stateProv': patient.stateProv,
                'zipCode': patient.zipCode,
                'hospital': patient.hospital,
                'height': patient.height,
                'weight': patient.weight,

                'emergency_first': patient.emergency_first,
                'emergency_last': patient.emergency_last,
                'emergency_phone': patient.emergency_phone,
                'insurance_num': patient.insurance_num,
                'insurance_name': patient.insurance_name
            })

        elif isDoctor:
            s = EditDoctorForm(initial={
                'email': user.email,
                'firstName': user.first_name,
                'lastName': user.last_name,

                'emergency_first': patient.emergency_first,
                'emergency_last': patient.emergency_last,
                'emergency_phone': patient.emergency_phone,
            })

        elif isNurse:
            s = EditDoctorForm(initial={
                'email': user.email,
                'firstName': user.first_name,
                'lastName': user.last_name,

                'emergency_first': patient.emergency_first,
                'emergency_last': patient.emergency_last,
                'emergency_phone': patient.emergency_phone,
            })

        elif isAdmin:
            s = EditAdminForm(initial={
                'email': user.email,
                'firstName': user.first_name,
                'lastName': user.last_name,
            })
    nn = []
    for notification in Notification.objects.all():
        if str(notification) == request.user.username:
            if notification.read == False:
                nn.append(notification)


    isPatient = userIsPatient(request.user)
    isDoctor = userIsDoctor(request.user)
    isNurse = userIsNurse(request.user)
    isAdmin = userIsAdmin(request.user)
    return render(request,'Register/edit.html', {
        'user': s,
        'firstName': request.user.first_name,
        'lastName': request.user.last_name,
        'isPatient' : isPatient,
        'isDoctor' : isDoctor,
        'isNurse' : isNurse,
        'isAdmin' : isAdmin,
        'notifications' : nn,
        'notifyLength' : len(nn),
        'id' : request.user.id,
    })

def password(request, theId):
    return render(request, 'Register/password.html')