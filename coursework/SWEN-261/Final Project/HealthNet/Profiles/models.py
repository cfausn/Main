from django.db import models
from django.contrib.auth.models import User
#from Medical_Info.models import *
from django import apps, forms
import datetime
from django.utils import timezone


#Declare constants
MAX_USERNAME_LENGTH = 14 #Max length for a username
MAX_PASSWORD_LENGTH = 35 #Max length for a password
MAX_STRING_LENGTH = 500 #Max length for any string not listed specifically here
PHONE_NUMBER_LENGTH = 15 #Max length for a phone number
ZIP_CODE_LENGTH = 6 #Max length for a zip code, also greatest length for a gender
MAX_BLOOD_PRESSURE_LENGTH = 7 # i = int; iii/iii eg. 120/80
MAX_BLOOD_TYPE_LENGTH = 3 # BT = O or AB or AB+
MAX_STRING_LENGTH_EXTENDED = 2500

"""
The hospital class represents a hospital within
"""

class Hospital(models.Model):
    name = models.CharField(max_length= MAX_STRING_LENGTH)
    address = models.CharField(max_length=MAX_STRING_LENGTH, default=None, null=True)
    def location(self):
        return self.address
    def __str__(self):
        return self.name

    def create_hospital(self, name):
        hospital = self.create(name= name)
        return hospital

class Doctor(models.Model):
    theUser = models.OneToOneField(User)
    middleName = models.CharField(max_length = MAX_STRING_LENGTH,null=True, blank=True) #User's Middle Name
    maxPatients = models.IntegerField
    emergency_first = models.CharField(max_length=MAX_STRING_LENGTH, null=True, blank=True)
    emergency_last = models.CharField(max_length=MAX_STRING_LENGTH, null=True, blank=True)
    emergency_phone = models.CharField(max_length=MAX_STRING_LENGTH, null=True, blank=True)
    max_patients = models.IntegerField(default=20)
    hospital = models.ManyToManyField(Hospital, default=None)

    def getType(self):
        return "Doctor"

    def __str__(self):
        return self.theUser.username

    def getName(self):
        return self.theUser.firstName + " " + self.theUser.lastName

    def createPrescription(self, patient, name, doses, comments):
        model = apps.get_model()
        prescription = Prescription(name,doses, self, comments, patient)
        patient.prescription.add(prescription)

    def create_doctor(self, user):
        doctor = self.create(theUser= user)
        return doctor




class Nurse(models.Model):
    theUser = models.OneToOneField(User)
    middleName = models.CharField(max_length = MAX_STRING_LENGTH,null=True, blank=True) #User's Middle Name
    phoneNumber = models.CharField(max_length = PHONE_NUMBER_LENGTH,null=True, blank=True) #User's Phone number without dashes
    emergency_first = models.CharField(max_length=MAX_STRING_LENGTH, null=True, blank=True)
    emergency_last = models.CharField(max_length=MAX_STRING_LENGTH, null=True, blank=True)
    emergency_phone = models.CharField(max_length=MAX_STRING_LENGTH, null=True, blank=True)
    hospital = models.ForeignKey(Hospital, default=None, blank=True, null=True)

    def getType(self):
        return "Nurse"

    def __str__(self):
        return self.theUser.username

    def create_nurse(self, user):
        nurse = self.create(theUser= user)
        return nurse



class Patient(models.Model):
    theUser = models.OneToOneField(User)
    doctor = models.ForeignKey(Doctor, default=None, blank=True, null=True)
    middleName = models.CharField(max_length = MAX_STRING_LENGTH,null=True, blank=True) #User's Middle Name
    suffix = models.CharField(max_length = MAX_STRING_LENGTH,null=True, blank=True) #User's Suffix (i.e. Jr. , Sr. , III)
    phoneNumber = models.CharField(max_length = PHONE_NUMBER_LENGTH,null=True, blank=True) #User's Phone number without dashes
    dateOfBirth = models.DateField ('Date of Birth', null=True, blank=True) #User's date of birth
    addressLine1 = models.CharField(max_length = MAX_STRING_LENGTH,null=True, blank=True) #User's address line 1, Street address, P.O. box, company name
    addressLine2 = models.CharField(max_length = MAX_STRING_LENGTH,null=True, blank=True) #User's address line 2, Apartment, suite, unit, building, floor, etc.
    city = models.CharField(max_length= MAX_STRING_LENGTH,null=True, blank=True) #user's city of residence
    stateProv = models.CharField(max_length=MAX_STRING_LENGTH,null=True, blank=True) #User's state/province of residence
    zipCode = models.CharField(max_length = ZIP_CODE_LENGTH,null=True, blank=True) #User's 6 digit zip code
    gender = models.CharField(max_length= ZIP_CODE_LENGTH, null=True, blank=True) #Max zip code length is the same as max gender string length
    hospital = models.ForeignKey(Hospital, default=None, blank=True, null=True)
    height = models.CharField(max_length= ZIP_CODE_LENGTH, default=None, blank=True, null=True) #patient's height as an int
    weight = models.CharField(max_length= ZIP_CODE_LENGTH, default=None, blank=True, null=True) #patient's weight as an int

    ethnicity = models.CharField(max_length=MAX_STRING_LENGTH, null=True, blank=True) #patient's ethnicity
    #tried to make this inherited but it didn't like my syntax... Maybe for future releases
    #(Doctors, Nurses, and Patients all need emergency info)
    emergency_first = models.CharField(max_length=MAX_STRING_LENGTH, null=True, blank=True, default=None)
    emergency_last = models.CharField(max_length=MAX_STRING_LENGTH, null=True, blank=True, default=None)
    emergency_phone = models.CharField(max_length=MAX_STRING_LENGTH, null=True, blank=True, default=None)
    insurance_num = models.CharField(max_length=MAX_STRING_LENGTH, null=True, blank=True, default=None)
    insurance_name = models.CharField(max_length=MAX_STRING_LENGTH, null=True, blank=True, default=None)
    #ALL OF THE FOLLOWING IS MEDICAL INFO
    heart_rate = models.IntegerField(null=True, blank=True, default=None) #heart rate as in int in beats per minute
    blood_pressure = models.CharField(max_length=MAX_BLOOD_PRESSURE_LENGTH ,null=True, blank=True, default=None) #TODO verify this in form should be inputted as int/int
    blood_type = models.CharField(max_length=MAX_BLOOD_TYPE_LENGTH ,null=True, blank=True, default=None)
    frequent_smoker = models.BooleanField(default=False)
    frequent_drinker = models.BooleanField(default=False)
    cholesterol = models.IntegerField(null=True, blank=True)
    admitted_to = models.BooleanField(default=False)
    #/MEDICAL INFO
    isNew = models.BooleanField(default=True)


    def getType(self):
        return "Patient"
    def __str__(self):
        return self.theUser.username

    def create_patient(self, user, hospital, provider, insurance_number):
        patient = self.create(theUser= user, hospital= hospital, insurance_name= provider, insurance_num= insurance_number)
        return patient


class Prescription(models.Model):
    #This is the prescription, not the drug: So no expiration date
    name = models.CharField(max_length=MAX_STRING_LENGTH)
    doses = models.IntegerField(null=True)
    comments = models.CharField(max_length=MAX_STRING_LENGTH, blank=True, null=True)
    patient = models.ForeignKey(Patient, default=None)
    date = models.DateField(null=True, blank=True)
    in_use = models.BooleanField(default=True)

    def __str__(self):
        return self.name + ": " + str(self.patient) + " :" + str(self.date) #returns the name of the drug

    def displayInfo(self):
        """
        Prescription: %name
        Doses: %doses
        Comments: %comments
        Date: %date
        """
        return "Prescription: " + self.name + "\nDoses: " + str(self.doses) + "\nComments: " + self.comments + "\nDate: " + str(self.date)

    def createPrescription(self, patient, name, doses, comments):
        newPrescription = Prescription.objects.create()
        newPrescription.name = name
        newPrescription.patient = patient
        newPrescription.doses = doses
        newPrescription.comments = comments

class TestResults(models.Model):
    testName = models.CharField(max_length= MAX_STRING_LENGTH)
    isApproved = models.BooleanField(default=False) #TODO do not allow this to default to true for final R2
    patient = models.ForeignKey(Patient, default=None)
    date = models.DateField()
    image = models.FileField(null= True, blank=True)
    category = models.CharField(max_length = MAX_STRING_LENGTH, default = "uncategorized")
    testDetails = models.CharField(max_length=MAX_STRING_LENGTH_EXTENDED, null=True, blank=True)

    def __str__(self):
        return self.testName + ": " + str(self.patient) + ": " + str(self.date)

    def displayInfo(self):
        """
        #display only if approved
        Test Results: %testName
        Date: %date
        Details: %testDetails
        """
        return "Test Results: " + self.testName + "\nDate: " + str(self.date) + "\nDetails: " + self.testDetails

class Surgery(models.Model):
    surgeryName = models.CharField(max_length=MAX_STRING_LENGTH)
    date = models.DateField()
    surgeryDetails = models.CharField(max_length=MAX_STRING_LENGTH, null=True, blank=True)
    patient = models.ForeignKey(Patient, default=None)
    def getSurgeryHasHappened(self):
        """
        Get weather or not this surgery has happened
        :return: True if it has, False if it has not
        """
        return datetime.datetime.today() < self.date

    def __str__(self):
        return self.surgeryName + ": " + str(self.patient)  + ": " + str(self.date)

    def displayInfo(self):
        """
        Surgery: %name
        Date: %date
        Surgery Details: %details
        """
        return "Surgery: " +  self.surgeryName + "\n" + "Date: " + str(self.date) + "\n" + "Details: " + self.surgeryDetails

class Admin(models.Model):
    theUser = models.OneToOneField(User)

    def getType(self):
        return "Admin"

    def create_admin(self, user):
        admin = self.create(theUser= user)
        return admin

    def __str__(self):
        return self.theUser.username

#if user is admin -> True, else -> False
def userIsAdmin(User):
    for admin in Admin.objects.all():
        if admin.theUser == User:
            return True
    return False

#if user is nurse -> True, else -> False
def userIsNurse(User):
    for nurse in Nurse.objects.all():
        if nurse.theUser == User:
            return True
    return False

#if user is doctor -> True, else -> False
def userIsDoctor(User):
    for doctor in Doctor.objects.all():
        if doctor.theUser == User:
            return True
    return False

#if user is admin -> True, else -> False
def userIsPatient(User):
    for patient in Patient.objects.all():
        if patient.theUser == User:
            return True
    return False

def getDoctorIsAvailable(doctor):
    """
    Checks to see if a doctor is at or exceeding their number of max patients
    :param doctor: Doctor to check
    :return: True if the doctor is not at or exceeding the max, False otherwise
    """
    numPatients = doctor.patient_set.count()
    return ( numPatients < doctor.max_patients ) and doctor.theUser.is_active

def getAvailableDoctors(hospital):
    """
    Call to get which doctors are "available" a doctor is available if they are not at or exceeding their number
    of max patients
    :return: Array of available doctors as their associated user object
    """
    availableDoctors = []
    for doctor in Doctor.objects.all():
        if getDoctorIsAvailable(doctor) and hospital in doctor.hospital.all():
            availableDoctors.append(doctor.theUser)
    return availableDoctors
# Create your models here.
