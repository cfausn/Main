from django import forms
from .models import TestResults, Surgery, userIsDoctor, userIsNurse, Patient, Prescription, Hospital, Admin, Nurse, Doctor
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class TestResultsForm(forms.ModelForm):
    testName = forms.CharField()
    testDetails = forms.CharField()
    patient = forms.ModelChoiceField(queryset=Patient.objects.all())
    class Meta:
        model = TestResults
        fields = ['testName', 'patient', 'testDetails']

class SurgeryForm(forms.ModelForm):
    surgeryName = forms.CharField()
    date = forms.DateField(input_formats=['%Y-%m-%d'])
    surgeryDetails = forms.CharField()
    patient = forms.ModelChoiceField(queryset=Patient.objects.all())

    class Meta:
        model = Surgery
        fields = ['surgeryName', 'date', 'surgeryDetails', 'patient']

class PrescriptionForm(forms.ModelForm):
    def validate_doses(value):
        for i in range(0,len(value)):
                if value[i].isalpha():
                    raise ValidationError("Must only contain numbers")
    name = forms.CharField()
    doses = forms.CharField(validators=[validate_doses])
    comments = forms.CharField()

    class Meta:
        model = Prescription
        fields = ['name', 'doses', 'comments']

class CSVForm(forms.Form):
    csv = forms.FileField()

    def save(self):
        instance = getattr(self, "instance", None)
        if instance:
            instance.save()
        return instance


#TODO: http://stackoverflow.com/questions/6091965/django-upload-a-file-and-read-its-content-to-populate-a-model