from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import Http404
from .models import Appointment
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from django.db import models
from .forms import appointmentForm
from Profiles.models import *
from logs.models import Entry
import datetime
import logging
from notifications.models import Notification

def index(request):
    theId = request.user.id
    context = RequestContext(request)

    doctor = False
    patient = False
    account = None
    if userIsDoctor(request.user):
        doctor = True
        account = Doctor.objects.get(theUser = request.user)
    if userIsPatient(request.user):
        patient = True
        account = Patient.objects.get(theUser = request.user)

    appointments = []
    if account != None:
        for appointment in account.appointment_set.all():
            tempLst = []
            tempLst.append(appointment.comments)
            tempLst.append(appointment.description)
            tempLst.append(str(appointment.startDate))
            tempLst.append(str(appointment.startTime))
            tempLst.append(str(appointment.endDate))
            tempLst.append(str(appointment.endTime))


            appointments.append(tempLst)
    n = []

    for notification in Notification.objects.all():
        if str(notification) == request.user.username:
            if notification.read == False:
                n.append(notification)



    if request.method == "POST":
        s = appointmentForm(request.user, request.POST)

        if s.is_valid():

            tempLst = []

            tempLst.append(request.POST['comments'])
            tempLst.append(request.POST['description'])
            tempLst.append(request.POST['startDate'])
            tempLst.append(request.POST['startTime'])
            tempLst.append(request.POST['endDate'])
            tempLst.append(request.POST['endTime'])

            timeConflict = False

            for ap in appointments:
                if ap[2] == tempLst[2]:

                    if time_in_range(datetime.datetime.strptime(ap[3], "%H:%M:%S"),
                                     datetime.datetime.strptime(ap[5], "%H:%M:%S"),
                                     datetime.datetime.strptime(tempLst[3], "%H:%M")):
                        timeConflict = True


            if not timeConflict:
                appointments.append(tempLst)
                Entry.objects.new_entry(request.user, 'New appointment created by %s' % request.user.username, datetime.datetime.now())
                s.save()



            return render(request, 'Schedule/index.html', {

                'id' : theId,
                'firstName': request.user.first_name,
                'lastName': request.user.last_name,
                'appointment': s,
                'isDoctor': doctor,
                'isPatient': patient,
                'appointments': appointments,
                'notifications' : n,
                'notifyLength' : len(n),
            })


    else:
        s = appointmentForm(request.user)


    return render(request,'Schedule/index.html', {
        'id' : theId,
        'firstName': request.user.first_name,
        'lastName': request.user.last_name,
        'appointment': s,
        'isDoctor': doctor,
        'isPatient': patient,
        'appointments': appointments,
        'notifications' : n,
        'notifyLength' : len(n),
    })


def time_in_range(start, end, x):
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

def monthView(request, user_id, year, month):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    if (int(month) > 12):
        raise Http404("Month does not exist")
    context = RequestContext(request, {
        'month': month,
        'year': year,
    })
    return render(request, 'Schedule/monthView.html', context)

def yearView(request, user_id, year):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    context = RequestContext(request, {
        'year': year,
    })
    return render(request, 'Schedule/yearView.html', context)

def deleteAppointment(request, appointment_id):
    appointment = Appointment.objects.get(pk=appointment_id)
    if request.user not in appointment.usersInvolved.all() and not userIsAdmin(request.user):
        return render(request, 'Schedule/deleteDenied.html')
    else:
        logging.info("Appointment deleted " + str(appointment))
        appointment.delete()
    return render(request, 'Schedule/deleteAppointment.html')

def scheduleDetails(request, user_id, year, month, day):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    schedule = []
    account = None
    if userIsPatient(user):
        account = Patient.objects.get(theUser=user)
    elif userIsDoctor(user):
        account = Doctor.objects.get(theUser=user)
    for appointment in account.appointment_set.all():
        if int(year) == appointment.startTime.year:
            if int(month) == appointment.startTime.month:
                if int(day) == appointment.startTime.day:
                    schedule.append(appointment)
    nextDayUrl = "/Schedule/" + getNextDayUrl(month, day, year) + user_id
    prevDayUrl = "/Schedule/" + getPrevDayUrl(month, day, year) + user_id
    nextWeekUrl = "/Schedule/" + getNextWeekUrl(month, day, year) + user_id
    prevWeekUrl = "/Schedule/" + getPrevWeekUrl(month, day, year) + user_id
    nextYearUrl = "/Schedule/" + getNextYearUrl(month, day, year) + user_id
    prevYearUrl = "/Schedule/" + getPrevYearUrl(month, day, year) + user_id
    context = RequestContext(request, {
        'username': user.username,
        'day': day,
        'month': month,
        'year': year,
        'schedule': schedule,
        'nextDayUrl': nextDayUrl,
        'prevDayUrl': prevDayUrl,
        'prevWeekUrl': prevWeekUrl,
        'nextWeekUrl': nextWeekUrl,
        'nextYearUrl': nextYearUrl,
        'prevYearUrl': prevYearUrl,
        'user_id': user.pk,
    })
    return render(request, 'Schedule/schedule.html', context)

def createAppointmentWith(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    if user == request.user:
        return render(request, 'Schedule/userError.html')
    if request.method == "POST":
        s = appointmentForm(request.POST)
        if s.is_valid():

            s.save()

            # CREATE NEW LOG ENTRY
            logging.info("New Appointment created: " + str(s))

            return render(request, 'Schedule/posted.html')
    else:
        s = appointmentForm()
    return render(request,'Schedule/createAppointment.html', {
        'appointment': s
    })

def createAppointment(request):
    if request.method == "POST":
        s = appointmentForm(request.user, request.POST)

        if s.is_valid():
            s.save()

            # CREATE NEW LOG ENTRY
            Entry.objects.new_entry(request.user, 'New appointment created by %s' % request.user.username, datetime.datetime.now())

            return render(request, 'Schedule/posted.html')
    else:
        user = request.user
        s = appointmentForm(request.user)

    return render(request,'Schedule/createAppointment.html', {
        'appointment': s
    })

def apppointmentDetails(request, appointment_id):
    try:
        appointment = Appointment.objects.get(pk=appointment_id)
    except Appointment.DoesNotExist:
        raise Http404("Appointment does not exist")
    usersInvolved = []
    usersInvolved = appointment.usersInvolved.all()
    context = RequestContext(request, {
        'appointment': appointment,
        'usersInvolved': usersInvolved,
        'appointment_id': appointment_id,
    })
    return render(request, 'Schedule/appointment.html', context)

def editAppointment(request, appointment_id):
    appointment = Appointment.objects.get(pk=appointment_id)
    if request.user not in appointment.usersInvolved.all() and not userIsAdmin(request.user) and not userIsNurse(request.user):
        return render(request, 'Schedule/accessDenied.html')
    if request.method == "POST":
        s = appointmentForm(request.POST, instance=Appointment.objects.get(pk=appointment_id))
        if s.is_valid():
            s.save()
            # CREATE NEW LOG ENTRY
            logging.info("Appointment Edited: " + str(s))


            return render(request, 'Schedule/posted.html')
    else:
        appointment = Appointment.objects.get(pk=appointment_id)
        s = appointmentForm(initial={
            'startTime': appointment.startTime,
            'endTime': appointment.endTime,
            'usersInvolved': appointment.usersInvolved.all(),
            'description': appointment.description,
            'comments': appointment.comments
        })
    return render(request,'Schedule/edit.html', {
        'user': s
    })


def getNextYearUrl(month, day, year):
    if (int(month) == 2 & int(year) % 4 == 0 and int(day) == 29):
        newMonth = str(3)
        newDay = str(1)
    else:
        newMonth = str(month)
        newDay = str(day)
    newYear = int(year) + 1
    return str(newYear) + "/" + newMonth + "/" + newDay + "/"

def getPrevYearUrl(month, day, year):
    if (int(month) == 2 & int(year) % 4 == 0 and int(day) == 29):
        newMonth = str(3)
        newDay = str(1)
    else:
        newMonth = str(month)
        newDay = str(day)
    newYear = int(year) - 1
    return str(newYear) + "/" + newMonth + "/" + newDay + "/"

def getPrevDayUrl(month, day, year):
    month = int(month)
    day = int(day)
    year = int(year)
    newDay = 0
    newMonth = 0
    newYear = 0
    if month == 3:
        if (day > 1):
            newMonth = str(month)
            newYear = str(year)
            newDay = str(day - 1)
        else:
            if (year % 4 == 0):
                newMonth = str(month - 1)
                newYear = str(year)
                newDay = str(29)
            else:
                newMonth = str(month - 1)
                newYear = str(year)
                newDay = str(28)
    elif month == 1:
        if (day > 1):
            newMonth = str(month)
            newYear = str(year)
            newDay = str(day - 1)
        else:
            newMonth = str(12)
            newYear = str(year - 1)
            newDay = str(31)
    elif month in [10,5,7,12]:
        if (day > 1):
            newMonth = str(month)
            newYear = str(year)
            newDay = str(day - 1)
        else:
            newMonth = str(month - 1)
            newYear = str(year)
            newDay = str(30)
    else:
        if (day > 1):
            newMonth = str(month)
            newYear = str(year)
            newDay = str(day - 1)
        else:
            newMonth = str(month - 1)
            newYear = str(year)
            newDay = str(31)
    return newYear + "/" + newMonth + "/" + newDay + "/"

def getNextDayUrl(month, day, year):
    month = int(month)
    day = int(day)
    year = int(year)
    newDay = 0
    newMonth = 0
    newYear = 0
    if month == 2:
        if (day < 28 or (year % 4 == 0 and day < 29) ):
            newMonth = str(month)
            newYear = str(year)
            newDay = str(day + 1)
        else:
            newMonth = str(month + 1)
            newYear = str(year)
            newDay = str(1)
    elif month == 12:
        if (day < 31):
            newMonth = str(month)
            newYear = str(year)
            newDay = str(day + 1)
        else:
            newMonth = str(1)
            newYear = str(year + 1)
            newDay = str(1)
    elif month in [9,4,6,11]:
        if (day < 30):
            newMonth = str(month)
            newYear = str(year)
            newDay = str(day + 1)
        else:
            newMonth = str(month + 1)
            newYear = str(year)
            newDay = str(1)
    else:
        if (day < 31):
            newMonth = str(month)
            newYear = str(year)
            newDay = str(day + 1)
        else:
            newMonth = str(month + 1)
            newYear = str(year)
            newDay = str(1)
    return newYear + "/" + newMonth + "/" + newDay + "/"

def getPrevDay(month, day, year):
    month = int(month)
    day = int(day)
    year = int(year)
    newDay = 0
    newMonth = 0
    newYear = 0
    if month == 3:
        if (day > 1):
            newMonth = str(month)
            newYear = str(year)
            newDay = str(day - 1)
        else:
            if (year % 4 == 0):
                newMonth = str(month - 1)
                newYear = str(year)
                newDay = str(29)
            else:
                newMonth = str(month - 1)
                newYear = str(year)
                newDay = str(28)
    elif month == 1:
        if (day > 1):
            newMonth = str(month)
            newYear = str(year)
            newDay = str(day - 1)
        else:
            newMonth = str(12)
            newYear = str(year - 1)
            newDay = str(31)
    elif month in [10,5,7,12]:
        if (day > 1):
            newMonth = str(month)
            newYear = str(year)
            newDay = str(day - 1)
        else:
            newMonth = str(month - 1)
            newYear = str(year)
            newDay = str(30)
    else:
        if (day > 1):
            newMonth = str(month)
            newYear = str(year)
            newDay = str(day - 1)
        else:
            newMonth = str(month - 1)
            newYear = str(year)
            newDay = str(31)

    return (newMonth, newDay, newYear)

def getPrevWeekUrl(month, day, year):
    for i in range (0,7):
        month, day, year = getPrevDay(month, day, year)
    return str(year) + "/" + str(month) + "/" + str(day) + "/"

def getNextDay(month, day, year):
    month = int(month)
    day = int(day)
    year = int(year)
    newDay = 0
    newMonth = 0
    newYear = 0
    if month == 2:
        if (day == 29):
            newMonth = str(month + 1)
            newYear = str(year)
            newDay = str(1)
        elif (day < 28 or ((year % 4 == 0 & day < 29)) ):
            newMonth = str(month)
            newYear = str(year)
            newDay = str(day + 1)
        else:
            newMonth = str(month + 1)
            newYear = str(year)
            newDay = str(1)
    elif month == 12:
        if (day < 31):
            newMonth = str(month)
            newYear = str(year)
            newDay = str(day + 1)
        else:
            newMonth = str(1)
            newYear = str(year + 1)
            newDay = str(1)
    elif month in [9,4,6,11]:
        if (day < 30):
            newMonth = str(month)
            newYear = str(year)
            newDay = str(day + 1)
        else:
            newMonth = str(month + 1)
            newYear = str(year)
            newDay = str(1)
    else:
        if (day < 31):
            newMonth = str(month)
            newYear = str(year)
            newDay = str(day + 1)
        else:
            newMonth = str(month + 1)
            newYear = str(year)
            newDay = str(1)
    return (newMonth, newDay, newYear)

def getNextWeekUrl(month, day, year):
    for i in range (0,7):
        month, day, year = getNextDay(month, day, year)
    return str(year) + "/" + str(month) + "/" + str(day) + "/"

#returns false if appointments conflict
def checkAppointmentConflicts(appointment):
    for user in appointment.usersInvolved.all():
        for userAppointment in user.appointment_set.all():
            if checkAppointmentsCanCoexist(appointment, userAppointment) == False:
                return False
    return True

#returns false if appointments cannot coexist
def checkAppointmentsCanCoexist(appointment1, appointment2):
    a1StartHour = appointment1.startTime.hour
    a2StartHour = appointment2.startTime.hour
    a1EndHour = appointment1.endTime.hour
    a2EndHour = appointment2.endTime.hour
    a1StartMinute = appointment1.startTime.minute
    a2StartMinute = appointment2.startTime.minute
    a1EndMinute = appointment1.endTime.minute
    a2EndMinute = appointment2.endTime.minute
    for h in range(a1StartHour + 1, a1EndHour):
        if h == a2StartHour or h == a2EndHour:
            return False
    for t in range(a2StartHour + 1, a2EndHour):
        if h == a1StartHour or h == a1EndHour:
            return False
    if (a1StartHour == a2EndHour):
        if (a1StartMinute < a2EndMinute):
            return False
    if (a2StartHour == a1EndHour):
        if (a2StartMinute < a1EndMinute):
            return False
    return True

