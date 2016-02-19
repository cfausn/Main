from django.shortcuts import render
from logs.models import Entry
from django.template import RequestContext, loader

from django.http import HttpResponse, Http404
from .models import *
from django.contrib.auth.models import User
import datetime
from notifications.models import Notification
from Register.forms import PatientForm, NurseForm, DoctorForm, AdminForm, HospitalForm
from django.contrib.auth.decorators import login_required
from django import template
from django.contrib.auth.models import User
import logging
from Schedule.models import Appointment

from .forms import PrescriptionForm, SurgeryForm, TestResultsForm, CSVForm

register = template.Library()
@register.simple_tag
def get_username_from_userid(user_id):
    try:
        return User.objects.get(id=user_id).username
    except User.DoesNotExist:
        return 'Unknown'


def quickSortByDate(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[int((len(lst)-1)/2)]
    lst.remove(pivot)
    less = []
    greater = []
    for info in lst:
        if info.date <= pivot.date:
            less.append(info)
        else:
            greater.append(info)
    return quickSortByDate(less) + [pivot] + quickSortByDate(greater)

@login_required(login_url='/../')
def index(request):
    users = []
    isAdmin = True
    targetUsername = request.user
    theId = request.user.id
    notifyP = False
    notifyN = False
    notifyD = False
    notifyA = False
    notifyH = False
    p = None
    n = None
    d = None
    a = None
    h = None
    isPatient = False
    isDoctor = False
    isNurse = False


    isPatient = userIsPatient(targetUsername)
    isAdmin = userIsAdmin(targetUsername)
    isDoctor = userIsDoctor(targetUsername)
    isNurse = userIsNurse(targetUsername)

    if request.method == "POST" and 'patient' in request.POST:
        p = PatientForm(request.POST)
        if p.is_valid():
            p.save()
            notifyP = True
            n = NurseForm()
            d = DoctorForm()
            a = AdminForm()
            h = HospitalForm()

    elif request.method == "POST" and 'nurse' in request.POST:
        n = NurseForm(request.POST)
        if n.is_valid():
            n.save()
            notifyN = True
            p = PatientForm()
            d = DoctorForm()
            a = AdminForm()
            h = HospitalForm()

    elif request.method == "POST" and 'doctor' in request.POST:
        d = DoctorForm(request.POST)
        if d.is_valid():
            d.save()
            notifyD = True
            p = PatientForm()
            n = NurseForm()
            a = AdminForm()
            h = HospitalForm()

    elif request.method == "POST" and 'admin' in request.POST:
        a = AdminForm(request.POST)
        if a.is_valid():
            a.save()
            notifyA = True
            p = PatientForm()
            n = NurseForm()
            d = DoctorForm()
            h = HospitalForm()

    elif request.method == "POST" and 'hospital' in request.POST:
        h = HospitalForm(request.POST)
        if h.is_valid():
            h.save()
            notifyH = True
            Entry.objects.new_entry(targetUsername, 'New Hospital created' , datetime.datetime.now())
            p = PatientForm()
            n = NurseForm()
            d = DoctorForm()
            a = AdminForm()
    else:
        p = PatientForm()
        n = NurseForm()
        d = DoctorForm()
        a = AdminForm()
        h = HospitalForm()

    if request.method == "POST" and 'delete' in request.POST:

        userToDelete = request.POST.get('userDelete')

        tempLst = userToDelete.split(',')

        for user in User.objects.all():
            if user.username == tempLst[1]:
                user.is_active = False
                user.save()

    for patient in Patient.objects.all():
        if patient.theUser.is_active == True:
            users.append(patient)
    for doctor in Doctor.objects.all():
        if doctor.theUser.is_active == True:
            users.append(doctor)
    for nurse in Nurse.objects.all():
        if nurse.theUser.is_active == True:
            users.append(nurse)
    for admin in Admin.objects.all():
        if admin.theUser != request.user and admin.theUser.is_active == True:
            users.append(admin)


    nn = []
    for notification in Notification.objects.all():
        if str(notification) == request.user.username:
            if notification.read == False:
                nn.append(notification)



    context = RequestContext(request, {
        'id' : theId,
        'userList': users,
        'username' : targetUsername,
        'isAdmin': isAdmin,
        'isPatient': isPatient,
        'isDoctor': isDoctor,
        'isNurse': isNurse,
        'today': datetime.datetime.today(),
        'p' : p,
        'n' : n,
        'd' : d,
        'a' : a,
        'h':h,
        'notifyP': notifyP,
        'notifyN': notifyN,
        'notifyD': notifyD,
        'notifyA': notifyA,
        'notifyH': notifyH,
        'notifications' : nn,
        'notifyLength' : len(nn),
    })
    return render(request, 'Profiles/index.html', context)




@login_required(login_url='/../')
def profile(request,theId):
    guser = None

    for user in User.objects.all():
        if user.id == int(theId):
            guser = user

    if guser==None:
        raise Http404("User not found")



    userIsRequestUser = ( request.user == guser )

    isPatient = userIsPatient(guser)
    isDoctor = userIsDoctor(guser)
    isNurse = userIsNurse(guser)
    isAdmin = userIsAdmin(guser)
    targetUsername = get_username_from_userid(theId)

    requestPatient = False
    requestDoctor = False
    requestNurse = False
    requestAdmin = False
    #different permissions for different users (highest level of permissions here is Doctor)

    for patient in Patient.objects.all():
        if request.user == patient.theUser:
            requestPatient = True

    for doctor in Doctor.objects.all():
        if request.user == doctor.theUser:
            requestDoctor = True

    for nurse in Nurse.objects.all():
        if request.user == nurse.theUser:
            requestNurse = True
            requestNurse = True

    for admin in Admin.objects.all():
        if request.user == admin.theUser:
            requestAdmin = True


    doctorOf = False

    if isPatient:
        if requestPatient and not userIsRequestUser:
            return render(request, 'Profiles/redirectProfile.html', {})
        if requestDoctor:
            doctorProfile = None
            for doctor in Doctor.objects.all():
                if doctor.theUser == request.user:
                    doctorProfile = doctor
            if doctorProfile != None:
                doctorOf = False
                for patient in doctorProfile.patient_set.all():
                    if patient.theUser == guser:
                        doctorOf = True
            else:
                doctorOf = False
    n = []

    p = None


    for notification in Notification.objects.all():
        if str(notification) == request.user.username:
            if notification.read == False:
                n.append(notification)

    for patient in Patient.objects.all():
            if patient.theUser == guser:
                p = patient

    for doctor in Doctor.objects.all():
            if doctor.theUser == guser:
                p = doctor

    for nurse in Nurse.objects.all():
            if nurse.theUser == guser:
                p = nurse

    for admin in Admin.objects.all():
            if admin.theUser == guser:
                p = admin

    if isPatient:
        medicalInfo = []
        surgeries = []
        results = []
        prescriptions = []

        for surgery in Surgery.objects.filter(patient = p):
            medicalInfo.append(surgery)
            surgeries.append(surgery)

        for test in TestResults.objects.filter(patient = p):
            medicalInfo.append(test)
            results.append(test)

        for prescription in Prescription.objects.filter(patient = p):
            medicalInfo.append(prescription)
            prescriptions.append(prescription)
        medicalInfo = quickSortByDate(medicalInfo)
        surgeries = quickSortByDate(surgeries)
        results = quickSortByDate(results)
        prescriptions = quickSortByDate(prescriptions)

        context = RequestContext(request, {
            'idd': theId,
            'id': request.user.id,
            'username': targetUsername,
            'isPatient': requestPatient,
            'isDoctor': requestDoctor,
            'isNurse': requestNurse,
            'isAdmin': requestAdmin,
            'userIsRequestUser': userIsRequestUser,
            'firstName': guser.first_name,
            'lastName': guser.last_name,
            'user_id': guser.pk,
            'today': datetime.datetime.today(),
            'notifications': n,
            'notifyLength': len(n),
            'requestPatient': requestPatient,
            'requestDoctor': requestDoctor,
            'requestNurse': requestNurse,
            'requestAdmin': requestAdmin,
            'middleName': p.middleName,
            'suffix': p.suffix,
            'hospital': p.hospital,
            'phoneNumber': p.phoneNumber,
            'addressLine1': p.addressLine1,
            'addressLine2': p.addressLine2,
            'dateOfBirth': p.dateOfBirth,
            'city': p.city,
            'stateProv': p.stateProv,
            'zipCode': p.zipCode,
            'height': p.height,
            'weight': p.weight,
            'gender': p.gender,
            'insurance_name': p.insurance_name,
            'insurance_num': p.insurance_num,
            'emergency_first': p.emergency_first,
            'emergency_last': p.emergency_last,
            'emergency_phone': p.emergency_phone,
            'doctor': p.doctor,
            'medicalInfo': medicalInfo,
            'heart_rate': p.heart_rate,
            'blood_pressure': p.blood_pressure,
            'frequent_smoker': p.frequent_smoker,
            'frequent_drinker': p.frequent_drinker,
            'cholesterol': p.cholesterol,
            'doctorOf': doctorOf,
            'surgeries': surgeries,
            'results': results,
            'prescriptions': prescriptions,
            'profilePatient': True,
            })
    elif isDoctor:
        context = RequestContext(request, {
            'idd': theId,
            'id': request.user.id,
            'username': targetUsername,
            'isPatient': requestPatient,
            'isDoctor': requestDoctor,
            'isNurse': requestNurse,
            'isAdmin': requestAdmin,
            'userIsRequestUser': userIsRequestUser,
            'firstName': guser.first_name,
            'lastName': guser.last_name,
            'user_id': guser.pk,
            'today': datetime.datetime.today(),
            'notifications': n,
            'notifyLength': len(n),
            'requestPatient': requestPatient,
            'requestDoctor': requestDoctor,
            'requestNurse': requestNurse,
            'requestAdmin': requestAdmin,
            'emergency_first': p.emergency_first,
            'emergency_last': p.emergency_last,
            'emergency_phone': p.emergency_phone,
            'hospital': p.hospital.all(),
            'doctorOf': doctorOf,
            'profilePatient': False,
            })
    elif isNurse:
        context = RequestContext(request, {
            'idd': theId,
            'id': request.user.id,
            'username': targetUsername,
            'isPatient': requestPatient,
            'isDoctor': requestDoctor,
            'isNurse': requestNurse,
            'isAdmin': requestAdmin,
            'userIsRequestUser': userIsRequestUser,
            'firstName': guser.first_name,
            'lastName': guser.last_name,
            'user_id': guser.pk,
            'today': datetime.datetime.today(),
            'notifications': n,
            'notifyLength': len(n),
            'requestPatient': requestPatient,
            'requestDoctor': requestDoctor,
            'requestNurse': requestNurse,
            'requestAdmin': requestAdmin,
            'emergency_first': p.emergency_first,
            'emergency_last': p.emergency_last,
            'emergency_phone': p.emergency_phone,
            'doctorOf': doctorOf,
            'profilePatient': False,
            })
    elif isAdmin:
        context = RequestContext(request, {
            'idd': theId,
            'id': request.user.id,
            'username': targetUsername,
            'isPatient': requestPatient,
            'isDoctor': requestDoctor,
            'isNurse': requestNurse,
            'isAdmin': requestAdmin,
            'userIsRequestUser': userIsRequestUser,
            'firstName': guser.first_name,
            'lastName': guser.last_name,
            'user_id': guser.pk,
            'today': datetime.datetime.today(),
            'notifications': n,
            'notifyLength': len(n),
            'requestPatient': requestPatient,
            'requestDoctor': requestDoctor,
            'requestNurse': requestNurse,
            'requestAdmin': requestAdmin,
            'doctorOf': doctorOf,
            'profilePatient': False,
        })
    else:
        return render(request, 'Profiles/redirectProfile.html', {})

    return render(request, 'Profiles/profile.html', context)

@login_required(login_url='/../')
def log(request, theId):
    isAdmin = True
    n = []
    dateT = datetime.datetime.today().date()
    dateTom = dateT + datetime.timedelta(days=1)


    tempMonth = str(dateT.month)
    tempMonthTom = str(dateTom.month)
    tempDay = str(dateT.day)
    tempDayTom = str(dateTom.day)
    if len(tempMonth) == 1:
        tempMonth = "0" + tempMonth

    if len(tempDay) == 1:
        tempDay = "0" + tempDay

    if len(tempMonthTom) == 1:
        tempMonthTom = "0" + tempMonthTom

    if len(tempDayTom) == 1:
        tempDayTom = "0" + tempDayTom

    date = str(dateT.year) + "-" + tempMonth + "-" + tempDay
    dateE = str(dateTom.year) + "-" + tempMonthTom + "-" + tempDayTom


    for notification in Notification.objects.all():
        if str(notification) == request.user.username:
            if notification.read == False:
                n.append(notification)


    if request.POST:
        startDate = datetime.datetime.strptime(request.POST['startDate'], '%Y-%m-%d')
        endDate = datetime.datetime.strptime(request.POST['endDate'], '%Y-%m-%d')
        context = Entry.objects.filter(date__range=(startDate,endDate))

    else:
        context = Entry.objects.all().order_by('-id')



    return render(request, 'Profiles/log.html', {
        'idd': theId,
        'id': request.user.id,
        'context' : context,
        'isAdmin': isAdmin,
        'notifications' : n,
        'notifyLength' : len(n),
        'date': date,
        'dateE': dateE,
    })



@login_required(login_url='/../')
def mypatients(request, theId):
    guser = None
    p = None
    for user in User.objects.all():
        if user.id == int(theId):
            guser = user
    for doctor in Doctor.objects.all():
            if doctor.theUser == guser:
                p = doctor
    users = []
    isDoctor = True

    n = []
    for notification in Notification.objects.all():
        if str(notification) == request.user.username:
            if notification.read == False:
                n.append(notification)

    for patient in Patient.objects.all():
        if patient.doctor == p:
            users.append(patient.theUser)

    context = RequestContext(request, {
        'idd': theId,
        'id': request.user.id,
        'userList': users,
        'isDoctor': isDoctor,
        'today': datetime.datetime.today(),
        'notifications' : n,
        'notifyLength' : len(n),
    })
    return render(request, 'Profiles/mypatients.html', context)

@login_required(login_url='/../')
def dashboard(request):
    targetUsername = request.user
    theId = targetUsername.id
    isPatient = userIsPatient(request.user)
    isDoctor = userIsDoctor(request.user)
    isNurse = userIsNurse(request.user)
    isAdmin = userIsAdmin(request.user)
    user = User.objects.get(username=request.user)
    p = None

    p = None
    for patient in Patient.objects.all():
            if patient.theUser == user:
                p = patient

    if p:
        if p.isNew:
            setattr(p, 'isNew', False)
            p.save()
            Notification.objects.new_entry(p.theUser, "Click here to finish your Profile!", datetime.datetime.now(),
                                           "/Register/edit", 1, False)


    n = []

    for notification in Notification.objects.all():
        if str(notification) == request.user.username:
            if notification.read == False:
                n.append(notification)

    context = RequestContext(request,{
            'firstName': request.user.first_name,
            'lastName': request.user.last_name,
            'id' : theId,
            'username' : targetUsername,
            'isPatient' : isPatient,
            'isDoctor' : isDoctor,
            'isNurse' : isNurse,
            'isAdmin' : isAdmin,
            'myProfileUrl': getProfileUrl(targetUsername),
            'myScheduleUrl': getScheduleUrl(targetUsername),
            'notifications' : n,
            'notifyLength' : len(n),
        }
    )

    return render(request, 'Profiles/dashboard.html', context)

def export(request, theId):

    guser = None

    for user in User.objects.all():
        if user.id == int(theId):
            guser = user

    if guser==None:
        raise Http404("User not found")

    userIsRequestUser = ( request.user == guser )

    isPatient = userIsPatient(guser)
    isDoctor = userIsDoctor(guser)
    isNurse = userIsNurse(guser)
    isAdmin = userIsAdmin(guser)
    targetUsername = get_username_from_userid(theId)

    requestPatient = False
    requestDoctor = False
    requestNurse = False
    requestAdmin = False
    #different permissions for different users (highest level of permissions here is Doctor)

    for patient in Patient.objects.all():
        if request.user == patient.theUser:
            requestPatient = True

    for doctor in Doctor.objects.all():
        if request.user == doctor.theUser:
            requestDoctor = True

    for nurse in Nurse.objects.all():
        if request.user == nurse.theUser:
            requestNurse = True

    for admin in Admin.objects.all():
        if request.user == admin.theUser:
            requestAdmin = True

    doctorOf = False

    for patient in Patient.objects.all():
            if patient.theUser == guser:
                p = patient

    for doctor in Doctor.objects.all():
            if doctor.theUser == guser:
                p = doctor

    for nurse in Nurse.objects.all():
            if nurse.theUser == guser:
                p = nurse

    for admin in Admin.objects.all():
            if admin.theUser == guser:
                p = admin

    if isPatient:
        if requestPatient and not userIsRequestUser:
            return render(request, 'Profiles/redirectProfile.html', {})
        if requestDoctor:
            doctorProfile = None
            for doctor in Doctor.objects.all():
                if doctor.theUser == request.user:
                    doctorProfile = doctor
            if doctorProfile != None:
                doctorOf = False
                for patient in doctorProfile.patient_set.all():
                    if patient.theUser == guser:
                        doctorOf = True
            else:
                doctorOf = False

    n = []

    for notification in Notification.objects.all():
        if str(notification) == request.user.username:
            if notification.read == False:
                n.append(notification)

    for patient in Patient.objects.all():
            if patient.theUser == guser:
                p = patient

    if isPatient:
        medicalInfo = []
        surgeries = []
        results = []
        prescriptions = []

        for surgery in Surgery.objects.filter(patient = p):
            medicalInfo.append(surgery)
            surgeries.append(surgery)

        for test in TestResults.objects.filter(patient = p):
            medicalInfo.append(test)
            results.append(test)

        for prescription in Prescription.objects.filter(patient = p):
            medicalInfo.append(prescription)
            prescriptions.append(prescription)
        medicalInfo = quickSortByDate(medicalInfo)
        surgeries = quickSortByDate(surgeries)
        results = quickSortByDate(results)
        prescriptions = quickSortByDate(prescriptions)

        context = RequestContext(request, {
            'id': theId,
            'username': targetUsername,
            'isPatient': requestPatient,
            'isDoctor': requestDoctor,
            'isNurse': requestNurse,
            'isAdmin': requestAdmin,
            'userIsRequestUser': userIsRequestUser,
            'firstName': guser.first_name,
            'lastName': guser.last_name,
            'user_id': guser.pk,
            'today': datetime.datetime.today(),
            'notifications': n,
            'notifyLength': len(n),
            'requestPatient': requestPatient,
            'requestDoctor': requestDoctor,
            'requestNurse': requestNurse,
            'requestAdmin': requestAdmin,
            'middleName': p.middleName,
            'suffix': p.suffix,
            'hospital': p.hospital,

            'phoneNumber': p.phoneNumber,
            'addressLine1': p.addressLine1,
            'addressLine2': p.addressLine2,
            'dateOfBirth': p.dateOfBirth,
            'city': p.city,
            'stateProv': p.stateProv,
            'zipCode': p.zipCode,
            'height': p.height,
            'weight': p.weight,
            'gender': p.gender,

            'insurance_name': p.insurance_name,
            'insurance_num': p.insurance_num,
            'emergency_first': p.emergency_first,
            'emergency_last': p.emergency_last,
            'emergency_phone': p.emergency_phone,
            'doctor': p.doctor,
            'medicalInfo': medicalInfo,
            'heart_rate': p.heart_rate,
            'blood_pressure': p.blood_pressure,
            'frequent_smoker': p.frequent_smoker,
            'frequent_drinker': p.frequent_drinker,
            'cholesterol': p.cholesterol,
            'doctorOf': doctorOf,

            'surgeries': surgeries,
            'results': results,
            'prescriptions': prescriptions,
            'profilePatient': True,
            })
    elif isDoctor:
        context = RequestContext(request, {
            'id': theId,
            'username': targetUsername,
            'isPatient': requestPatient,
            'isDoctor': requestDoctor,
            'isNurse': requestNurse,
            'isAdmin': requestAdmin,
            'userIsRequestUser': userIsRequestUser,
            'firstName': guser.first_name,
            'lastName': guser.last_name,
            'user_id': guser.pk,
            'today': datetime.datetime.today(),
            'notifications': n,
            'notifyLength': len(n),
            'requestPatient': requestPatient,
            'requestDoctor': requestDoctor,
            'requestNurse': requestNurse,
            'requestAdmin': requestAdmin,
            'emergency_first': p.emergency_first,
            'emergency_last': p.emergency_last,
            'emergency_phone': p.emergency_phone,
            'hospital': p.hospital.all(),
            'doctorOf': doctorOf,
            'profilePatient': False,
            })
    elif isNurse:
        context = RequestContext(request, {
            'id': theId,
            'username': targetUsername,
            'isPatient': requestPatient,
            'isDoctor': requestDoctor,
            'isNurse': requestNurse,
            'isAdmin': requestAdmin,
            'userIsRequestUser': userIsRequestUser,
            'firstName': guser.first_name,
            'lastName': guser.last_name,
            'user_id': guser.pk,
            'today': datetime.datetime.today(),
            'notifications': n,
            'notifyLength': len(n),
            'requestPatient': requestPatient,
            'requestDoctor': requestDoctor,
            'requestNurse': requestNurse,
            'requestAdmin': requestAdmin,
            'emergency_first': p.emergency_first,
            'emergency_last': p.emergency_last,
            'emergency_phone': p.emergency_phone,
            'doctorOf': doctorOf,
            'profilePatient': False,
            })
    elif isAdmin:
        context = RequestContext(request, {
            'id': theId,
            'username': targetUsername,
            'isPatient': requestPatient,
            'isDoctor': requestDoctor,
            'isNurse': requestNurse,
            'isAdmin': requestAdmin,
            'userIsRequestUser': userIsRequestUser,
            'firstName': guser.first_name,
            'lastName': guser.last_name,
            'user_id': guser.pk,
            'today': datetime.datetime.today(),
            'notifications': n,
            'notifyLength': len(n),
            'requestPatient': requestPatient,
            'requestDoctor': requestDoctor,
            'requestNurse': requestNurse,
            'requestAdmin': requestAdmin,
            'doctorOf': doctorOf,
            'profilePatient': False,
        })

    return render(request, 'Profiles/export.html', context)

def myPatients(request):
    #Doctors Only
    pass

def myDoctor(request):
    #Patients Only
    pass

def myPatientsDoctors(request):
    #Nurses Only
    pass

def getProfileUrl(user):
    return str(user.id) + "/profile"

def getScheduleUrl(user):
    id = str(user.pk)
    today = datetime.datetime.today()
    year = str(today.year)
    day = str(today.day)
    month = str(today.month)
    urlStr = year + "/" + month + "/" + day + "/" + id
    return urlStr

def getNextThreeAppointments(user):
    appointments = []
    for appointment in Appointment.objects.all():
        if (appointment.startTime > datetime.datetime.now()):
            appointments.append(appointment)
    nextThree = []
    for appointment in appointments:
        pass

    return nextThree

def createPrescription(request, theId):
    targetUsername = request.user
    targetId = targetUsername.id
    isPatient = userIsPatient(request.user)
    isDoctor = userIsDoctor(request.user)
    isNurse = userIsNurse(request.user)
    isAdmin = userIsAdmin(request.user)

    userToPrescribe = None

    for user in User.objects.all():
        if user.pk == int(theId):
            userToPrescribe = user

    patientToPrescribe = None

    for patient in Patient.objects.all():
        if patient.theUser.pk == int(theId):
            patientToPrescribe = patient

    if userToPrescribe == None:
        raise Http404("User not found")

    if patientToPrescribe == None:
        raise Http404("Patient not found")

    doctorOf = False

    if isDoctor:
        doctorProfile = None
        for doctor in Doctor.objects.all():
            if doctor.theUser == request.user:
                doctorProfile = doctor
        if doctorProfile != None:
            doctorOf = False
            for patient in doctorProfile.patient_set.all():
                if patient.theUser == userToPrescribe:
                    doctorOf = True
        else:
            doctorOf = False

    if (isPatient or isAdmin or (isDoctor and not doctorOf)):
        return render(request, 'Profiles/redirectProfile.html')

    n = []

    for notification in Notification.objects.all():
        if str(notification) == targetUsername.username:
            if notification.read == False:
                n.append(notification)

    if request.method == "POST":
        name = request.POST.get('name')
        doses = request.POST.get('doses')
        comments = request.POST.get('comments')

        if int(doses) < 0:
            doses = 0

        prescription = Prescription()
        prescription.name = name
        prescription.doses = int(doses)
        prescription.comments = comments
        prescription.patient = patientToPrescribe
        prescription.date = datetime.datetime.today()
        prescription.save()
        Entry.objects.new_entry(request.user, "Prescription created", datetime.datetime.now())
        return render(request, 'Profiles/redirectProfile.html', {})
    else:
        s = None
    return render(request,'Profiles/createPrescription.html', {
        'form': s,
        'username' : targetUsername,
        'isPatient' : isPatient,
        'isDoctor' : isDoctor,
        'isNurse' : isNurse,
        'isAdmin' : isAdmin,
        'id' : targetId,
        'notifications' : n,
        'notifyLength' : len(n),
    })

def createSurgery(request, theId):
    targetUsername = request.user
    id = targetUsername.id
    isPatient = userIsPatient(request.user)
    isDoctor = userIsDoctor(request.user)
    isNurse = userIsNurse(request.user)
    isAdmin = userIsAdmin(request.user)

    n = []

    userToPrescribe = None

    for user in User.objects.all():
        if user.pk == int(theId):
            userToPrescribe = user

    patientToPrescribe = None

    for patient in Patient.objects.all():
        if patient.theUser.pk == int(theId):
            patientToPrescribe = patient

    if userToPrescribe == None:
        raise Http404("User not found")

    if patientToPrescribe == None:
        raise Http404("Patient not found")

    doctorOf = False


    if isDoctor:
        doctorProfile = None
        for doctor in Doctor.objects.all():
            if doctor.theUser == request.user:
                doctorProfile = doctor
        if doctorProfile != None:
            doctorOf = False
            for patient in doctorProfile.patient_set.all():
                if patient.theUser == userToPrescribe:
                    doctorOf = True
        else:
            doctorOf = False

    if (isPatient or isAdmin or (isDoctor and not doctorOf)):
        return render(request, 'Profiles/redirectProfile.html')

    for notification in Notification.objects.all():
        if str(notification) == targetUsername.username:
            if notification.read == False:
                n.append(notification)

    if request.method == "POST":
        surgery = Surgery()
        surgery.date = request.POST.get('date')
        surgery.surgeryName = request.POST.get('name')
        surgery.surgeryDetails = request.POST.get('details')
        surgery.patient = patientToPrescribe
        surgery.save()
        # CREATE NEW LOG ENTRY
        Entry.objects.new_entry(request.user, "Surgery created", datetime.datetime.now())
        return render(request, 'Profiles/redirectProfile.html')
    else:
        s = None
    return render(request,'Profiles/createSurgery.html', {
        'form': s,
        'username' : targetUsername,
        'isPatient' : isPatient,
        'isDoctor' : isDoctor,
        'isNurse' : isNurse,
        'isAdmin' : isAdmin,
        'id' : id,
        'notifications' : n,
        'notifyLength' : len(n),
    })


def createTestResults(request, theId):
    targetUsername = request.user
    id = targetUsername.id
    isPatient = userIsPatient(request.user)
    isDoctor = userIsDoctor(request.user)
    isNurse = userIsNurse(request.user)
    isAdmin = userIsAdmin(request.user)

    n = []

    userToPrescribe = None

    for user in User.objects.all():
        if user.pk == int(theId):
            userToPrescribe = user

    patientToPrescribe = None

    for patient in Patient.objects.all():
        if patient.theUser.pk == int(theId):
            patientToPrescribe = patient

    if userToPrescribe == None:
        raise Http404("User not found")

    if patientToPrescribe == None:
        raise Http404("Patient not found")

    doctorOf = False


    if isDoctor:
        doctorProfile = None
        for doctor in Doctor.objects.all():
            if doctor.theUser == request.user:
                doctorProfile = doctor
        if doctorProfile != None:
            doctorOf = False
            for patient in doctorProfile.patient_set.all():
                if patient.theUser == userToPrescribe:
                    doctorOf = True
        else:
            doctorOf = False

    if (isPatient or isAdmin or (isDoctor and not doctorOf)):
        return render(request, 'Profiles/redirectProfile.html')

    for notification in Notification.objects.all():
        if str(notification) == targetUsername.username:
            if notification.read == False:
                n.append(notification)

    if request.method == "POST":
        testResult = TestResults()
        testResult.testName = request.POST.get('name')
        testResult.testDetails = request.POST.get('details')
        testResult.category = request.POST.get('category')
        testResult.date = datetime.datetime.today()
        testResult.patient = patientToPrescribe
        approved = request.POST.get('approved')
        if approved == "Yes":
            testResult.isApproved = True
        else:
            testResult.isApproved = False
        testResult.save()
        # CREATE NEW LOG ENTRY
        Entry.objects.new_entry(request.user, "Test results created", datetime.datetime.now())
        return render(request, 'Profiles/redirectProfile.html')
    else:
        s = None
    return render(request,'Profiles/createTestResults.html', {
        'form': s,
        'username' : targetUsername,
        'isPatient' : isPatient,
        'isDoctor' : isDoctor,
        'isNurse' : isNurse,
        'isAdmin' : isAdmin,
        'id' : id,
        'notifications' : n,
        'notifyLength' : len(n),
    })

def statistics(request):
    targetUsername = request.user
    theId = targetUsername.id
    isPatient = userIsPatient(request.user)
    isDoctor = userIsDoctor(request.user)
    isNurse = userIsNurse(request.user)
    isAdmin = userIsAdmin(request.user)

    n = []

    for notification in Notification.objects.all():
        if str(notification) == targetUsername.username:
            if notification.read == False:
                n.append(notification)


    numpatients = 0 #total number of patients
    numusers = 0
    numdoctors = 0
    numnurses = 0
    numadmins = 0
    numinactive = 0

    for user in User.objects.all():
        if user.is_active:
            numusers += 1
        else:
            numinactive += 1

    for patient in Patient.objects.all():
        if patient.theUser.is_active:
            numpatients += 1

    for doctor in Doctor.objects.all():
        if doctor.theUser.is_active:
            numdoctors += 1


    for nurse in Nurse.objects.all():
        if nurse.theUser.is_active:
            numnurses += 1

    for admin in Admin.objects.all():
        if admin.theUser.is_active:
            numadmins += 1


    surgeries = {}
    maxSurgeryNum = 0
    maxSurgery = None
    for surgery in Surgery.objects.all():
        if surgery.surgeryName in surgeries:
            surgeries[surgery.surgeryName] += 1
        else:
            surgeries[surgery.surgeryName] = 1
    for surgery in Surgery.objects.all():
        if surgeries[surgery.surgeryName] > maxSurgeryNum:
            maxSurgery = surgery.surgeryName
            maxSurgeryNum = surgeries[surgery.surgeryName]
    prescriptions = {}
    maxPrescriptionNum = 0
    maxPrescription = None
    for prescription in Prescription.objects.all():
        if prescription.name in prescriptions:
            prescriptions[prescription.name] += 1
        else:
            prescriptions[prescription.name] = 1
    for prescription in Prescription.objects.all():
        if prescriptions[prescription.name] > maxPrescriptionNum:
            maxPrescription = prescription.name
            maxPrescriptionNum = prescriptions[prescription.name]
    tests = {}
    maxTestNum = 0
    maxTest = None
    for test in TestResults.objects.all():
        if test.testName in tests:
            tests[test.testName] += 1
        else:
            tests[test.testName] = 1
    for test in TestResults.objects.all():
        if tests[test.testName] > maxTestNum:
            maxTest = test.testName
            maxTestNum = tests[test.testName]
    maxDocNum = 0
    maxDoc = None
    for doctor in Doctor.objects.all():
        if doctor.patient_set.count() > maxDocNum:
            maxDocNum = doctor.patient_set.count()
            maxDoc = doctor.theUser.first_name + " " + doctor.theUser.last_name
    maxHospitalNum = 0
    maxHospital = None
    for hospital in Hospital.objects.all():
        patientCount = 0
        for patient in Patient.objects.filter(hospital= hospital):
            patientCount += 1
        if patientCount > maxHospitalNum:
            maxHospitalNum = patientCount
            maxHospital = hospital.name
    numappointments = 0 #total number of appointments in system
    for appointment in Appointment.objects.all():
        numappointments += 1
    numhospitals = Hospital.objects.count()
    hospitals = Hospital.objects.all()
    context = RequestContext(request, {
        'firstName': request.user.first_name,
        'lastName': request.user.last_name,
        'id' : theId,
        'username' : targetUsername,
        'isPatient' : isPatient,
        'isDoctor' : isDoctor,
        'isNurse' : isNurse,
        'isAdmin' : isAdmin,
        'popDoc': maxDoc,
        'popDocNum': maxDocNum,
        'popTest': maxTest,
        'popTestNum': maxTestNum,
        'popSurgery': maxSurgery,
        'popSurgeryNum': maxSurgeryNum,
        'popPresc': maxPrescription,
        'popPrescNum': maxPrescriptionNum,
        'popHospital': maxHospital,
        'popHospitalNum': maxHospitalNum,
        'numUsers':numusers,
        'numPatients':numpatients,
        'numDoctors':numdoctors,
        'numNurses':numnurses,
        'numAdmins':numadmins,
        'numAppointments': numappointments,
        'hospitals': hospitals,
        'numHospitals': numhospitals,
        'notifications' : n,
        'notifyLength' : len(n),
        'numinactive' : numinactive
    })
    return render(request,'Profiles/statistics.html', context)


def handle_uploaded_line(user):
    user_type = user[0]
    email = user[1]
    password = user[2]
    first_name = user[3]
    last_name = user[4]
    hospital = user[5]
    insurance_provider = user[6]
    insurance_number = user[7]
    duplicate = False
    for account in User.objects.all():
        if account.username == email:
            duplicate = True


    hospitalDuplicate = False
    for hospitalE in Hospital.objects.all():
        if hospitalE.name == hospital:
            hospitalDuplicate = True
            hospital = hospitalE
    if hospitalDuplicate == False:
        if not hospital == 'nil':
            hospitalC = Hospital()
            hospitalC.name = hospital
            hospitalC.address = ""
            hospitalC.save()
            hospital = hospitalC
        else:
            hospital = None
    if duplicate == False:
        userO = User()
        userO.username = email
        userO.email = email
        userO.password = password
        userO.last_name = last_name
        userO.first_name = first_name

        if user_type == "Doctor":
            userO.save()
            doctor = Doctor()
            doctor.theUser = userO
            doctor.save()
        elif user_type == "Patient":
            userO.save()
            patient = Patient()
            patient.theUser = userO
            patient.hospital = hospital
            patient.insurance_name = insurance_provider
            patient.insurance_num = insurance_number
            patient.save()
        elif user_type == "Nurse":
            userO.save()
            nurse = Nurse()
            nurse.hospital = hospital
            nurse.theUser = userO
            nurse.save()
        elif user_type == "Admin":
            userO.save()
            admin = Admin()
            admin.theUser = userO
            admin.save()

def inputCSV(request):
    #TODO finish CSV functionality


    if request.method == "POST":
        form = CSVForm(request.POST, request.FILES)
        print(request.FILES['csv'])

        for line in request.FILES['csv']:
            tempArray = []
            tempString = ''
            for i in line:
                if chr(i) == ',' :
                    tempArray.append(tempString)
                    tempString = ""
                else:
                    tempString += chr(i)
                print(chr(i))
            tempArray.append(tempString)
            handle_uploaded_line(tempArray)

        if form.is_valid():
            form.save()

    else:
        form = CSVForm()
    return render(request,'Profiles/genericForm.html', {
        'form': form
    })

def chooseMyDoctor(request):
    targetUsername = request.user
    theId = targetUsername.id
    isPatient = userIsPatient(request.user)
    isDoctor = userIsDoctor(request.user)
    isNurse = userIsNurse(request.user)
    isAdmin = userIsAdmin(request.user)

    n = []

    for notification in Notification.objects.all():
        if str(notification) == targetUsername.username:
            if notification.read == False:
                n.append(notification)

    if request.method == "POST":

        userToChoose = request.POST.get('userChoose')
        tempLst = userToChoose.split(',')
        thePatient = None
        for patient in Patient.objects.all():
            if patient.theUser == request.user:
                thePatient = patient

        if thePatient != None:
            for doctor in Doctor.objects.all():
                if doctor.theUser.username == userToChoose:
                    thePatient.doctor = doctor
                    thePatient.save()
        return render(request, 'Profiles/redirectProfile.html', {})
    else:
        access = False
        for patient in Patient.objects.all():
            if patient.theUser == request.user:
                access = True
                thePatient = patient
        if access:
            hospital = thePatient.hospital
            doctorList = getAvailableDoctors(hospital)
            return render(request, 'Profiles/chooseMyDoctor.html', {
                'currentUser': request.user,
                'doctorList': doctorList,
                'username' : targetUsername,
                'isPatient' : isPatient,
                'isDoctor' : isDoctor,
                'isNurse' : isNurse,
                'isAdmin' : isAdmin,
                'id' : theId,
                'notifications' : n,
                'notifyLength' : len(n),
            })
        else:
            return render(request, 'Profiles/redirectProfile.html', {})

def inactiveUsers(request):
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
            if notification.read == False:
                n.append(notification)

    if request.method == "POST":

        userToChoose = request.POST.get('userReactivate')
        tempLst = userToChoose.split(',')

        for user in User.objects.all():
            if user.username == tempLst[0]:
                user.is_active = True
                user.save()

        return render(request, 'Profiles/redirectProfile.html', {})
    else:
        if access:
            userList = []
            for user in User.objects.all():
                if user.is_active == False:
                    userList.append(user)
            return render(request, 'Profiles/inactiveAccounts.html', {
                'userList': userList,
                'username' : targetUsername,
                'isPatient' : isPatient,
                'isDoctor' : isDoctor,
                'isNurse' : isNurse,
                'isAdmin' : isAdmin,
                'id' : theId,
                'notifications' : n,
                'notifyLength' : len(n),
            })
        else:
            return render(request, 'Profiles/redirectProfile.html', {})

def approveTestResults(request, theId):
    targetUsername = request.user
    id = targetUsername.id
    isPatient = userIsPatient(request.user)
    isDoctor = userIsDoctor(request.user)
    isNurse = userIsNurse(request.user)
    isAdmin = userIsAdmin(request.user)

    n = []

    userToPrescribe = None

    for user in User.objects.all():
        if user.pk == int(theId):
            userToPrescribe = user

    patientToPrescribe = None

    for patient in Patient.objects.all():
        if patient.theUser.pk == int(theId):
            patientToPrescribe = patient

    if userToPrescribe == None:
        raise Http404("User not found")

    if patientToPrescribe == None:
        raise Http404("Patient not found")

    doctorOf = False

    if isDoctor:
        doctorProfile = None
        for doctor in Doctor.objects.all():
            if doctor.theUser == request.user:
                doctorProfile = doctor
        if doctorProfile != None:
            doctorOf = False
            for patient in doctorProfile.patient_set.all():
                if patient.theUser == userToPrescribe:
                    doctorOf = True
        else:
            doctorOf = False

    targetName = userToPrescribe.first_name + " " + userToPrescribe.last_name

    if (isPatient or isAdmin or (isDoctor and not doctorOf)):
        return render(request, 'Profiles/redirectProfile.html')

    for notification in Notification.objects.all():
        if str(notification) == targetUsername.username:
            if notification.read == False:
                n.append(notification)

    tests = []

    for testResult in patientToPrescribe.testresults_set.all():
        if testResult.isApproved == False:
            tests.append(testResult)

    if request.method == "POST":

        testToApprove = request.POST.get('testApprove')
        tempLst = testToApprove.split(',')

        for test in TestResults.objects.all():
            if test.pk == int(tempLst[0]):
                test.isApproved = True
                test.save()
        return render(request, 'Profiles/redirectProfile.html', {})

    else:
        s = None
    return render(request,'Profiles/unapprovedTests.html', {
        'tests': tests,
        'form': s,
        'username' : targetUsername,
        'theId': theId,
        'isPatient' : isPatient,
        'isDoctor' : isDoctor,
        'isNurse' : isNurse,
        'isAdmin' : isAdmin,
        'id' : id,
        'notifications' : n,
        'notifyLength' : len(n),
        'patientName': targetName,
    })

def editMedicalInfo(request, theId):
    targetUsername = request.user
    targetId = targetUsername.id
    isPatient = userIsPatient(request.user)
    isDoctor = userIsDoctor(request.user)
    isNurse = userIsNurse(request.user)
    isAdmin = userIsAdmin(request.user)

    userToPrescribe = None

    for user in User.objects.all():
        if user.pk == int(theId):
            userToPrescribe = user

    patientToPrescribe = None

    for patient in Patient.objects.all():
        if patient.theUser.pk == int(theId):
            patientToPrescribe = patient

    if userToPrescribe == None:
        raise Http404("User not found")

    if patientToPrescribe == None:
        raise Http404("Patient not found")

    doctorOf = False

    if isDoctor:
        doctorProfile = None
        for doctor in Doctor.objects.all():
            if doctor.theUser == request.user:
                doctorProfile = doctor
        if doctorProfile != None:
            doctorOf = False
            for patient in doctorProfile.patient_set.all():
                if patient.theUser == userToPrescribe:
                    doctorOf = True
        else:
            doctorOf = False

    if (isPatient or isAdmin or (isDoctor and not doctorOf)):
        return render(request, 'Profiles/redirectProfile.html')

    n = []

    for notification in Notification.objects.all():
        if str(notification) == targetUsername.username:
            if notification.read == False:
                n.append(notification)

    if request.method == "POST":
        heart_rate = request.POST.get('heart_rate')
        blood_pressure = request.POST.get('blood_pressure')
        blood_type = request.POST.get('blood_type')
        cholesterol = request.POST.get('cholesterol')
        frequent_smoker = ( request.POST.get('frequent_smoker') == "Yes" )
        frequent_drinker = ( request.POST.get('frequent_drinker') == "Yes" )
        patientToPrescribe.heart_rate = heart_rate
        patientToPrescribe.blood_pressure = blood_pressure
        patientToPrescribe.cholesterol = cholesterol
        patientToPrescribe.frequent_drinker = frequent_drinker
        patientToPrescribe.frequent_smoker = frequent_smoker
        patientToPrescribe.save()
        return render(request, 'Profiles/redirectProfile.html', {})
    else:
        s = None
    return render(request,'Profiles/editMedicalInfo.html', {
        'firstName': userToPrescribe.first_name,
        'lastName': userToPrescribe.last_name,
        'form': s,
        'username' : targetUsername,
        'isPatient' : isPatient,
        'isDoctor' : isDoctor,
        'isNurse' : isNurse,
        'isAdmin' : isAdmin,
        'id' : targetId,
        'notifications' : n,
        'notifyLength' : len(n),
    })

def nurseIndex(request):
    targetUsername = request.user
    theId = targetUsername.id
    isPatient = userIsPatient(request.user)
    isDoctor = userIsDoctor(request.user)
    isNurse = userIsNurse(request.user)
    isAdmin = userIsAdmin(request.user)

    n = []

    for notification in Notification.objects.all():
        if str(notification) == targetUsername.username:
            n.append(notification)

    requestNurse = None

    for nurse in Nurse.objects.all():
        if nurse.theUser == request.user:
            requestNurse = nurse

    if isNurse and not requestNurse == None :
        userList = []
        for doctor in Doctor.objects.all():
            if doctor.theUser.is_active:
                sameHospital = False
                for hospital in doctor.hospital.all():
                    if hospital == requestNurse.hospital:
                        sameHospital = True
                if sameHospital == True:
                    userList.append(doctor)
        for patient in requestNurse.hospital.patient_set.all():
            if patient.theUser.is_active == True:
                userList.append(patient)
        return render(request, 'Profiles/nurseDoctorIndex.html', {
                'userList': userList,
                'username' : targetUsername,
                'isPatient' : isPatient,
                'isDoctor' : isDoctor,
                'isNurse' : isNurse,
                'isAdmin' : isAdmin,
                'id' : theId,
                'notifications' : n,
                'notifyLength' : len(n),
                'hospital': requestNurse.hospital,
        })

    else:
        return render(request, 'Profiles/redirectProfile.html', {})