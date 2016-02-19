from django import forms
from .models import Appointment
from Profiles.models import Patient, Doctor, Nurse, userIsDoctor, userIsNurse, userIsPatient
from django.contrib.auth.models import User
import datetime

MAX_STRING_LENGTH = 100

class appointmentForm(forms.ModelForm):

    description = forms.CharField(max_length=MAX_STRING_LENGTH, required=True)
    startDate = forms.DateField(required=True, widget=forms.DateInput(attrs={
        'type': 'date'
    }))
    startTime = forms.TimeField(required=True, widget=forms.TimeInput(attrs={
        'type':'time'
    }))
    endDate = forms.DateField(required=True, widget=forms.DateInput(attrs={
        'type': 'date'
    }))
    endTime = forms.TimeField(required=True, widget=forms.TimeInput(attrs={
        'type':'time'
    }))
    comments = forms.CharField(max_length=MAX_STRING_LENGTH)

    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), required=False)

    patient = forms.ModelChoiceField(queryset=Patient.objects.all(), widget=forms.Select, empty_label='None', required=False,
                                     initial=None)

    def __init__(self, user, *args, **kwargs):
        super(appointmentForm, self).__init__(*args, **kwargs)
        if userIsDoctor(user):
            doctor = Doctor.objects.get(theUser=user)
            self.doctor = doctor
            self.fields['patient'].queryset = doctor.patient_set.all()
        if userIsPatient(user):
            patient = Patient.objects.get(theUser=user)
            self.patient = patient
            for doctor in Doctor.objects.all():
                if patient in doctor.patient_set.all():
                    self.fields['doctor'].initial = doctor

    class Meta:
        model = Appointment
        fields = {'description', 'startTime', 'startDate', 'endTime', 'endDate', 'comments', 'doctor', 'patient'}


