from django.db import models
from Profiles.models import Doctor, Patient

#Declare constants
#from Profiles.models import Patient, Doctor

from django.contrib.auth.models import User
import datetime

MAX_STRING_LENGTH = 500

class Appointment(models.Model):
    startDate = models.DateField()
    startTime = models.TimeField()
    endDate = models.DateField()
    endTime = models.TimeField()
    description = models.CharField(max_length=MAX_STRING_LENGTH)
    comments = models.CharField(max_length=MAX_STRING_LENGTH, null = True, blank= True)
    doctor = models.ForeignKey(Doctor, blank=True, null=True)
    patient = models.ForeignKey(Patient, blank=True, null=True)

    def __str__(self):
        return self.description

    def create_appointment(self, startDate, startTime, endDate, endTime, description, comments, doctor, patient):
        appointment = self.create(startDate = startDate, startTime = startTime, endDate = endDate, endTime = endTime,
                                  description = description, comments = comments, doctor = doctor, patient = patient)
        return appointment

# Create your models here.