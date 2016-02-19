from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from Profiles.models import Patient, Hospital, Doctor, Nurse, Admin
from django.forms.extras.widgets import SelectDateWidget
from logs.models import Entry
import datetime
from django.core.exceptions import ValidationError
from django.http import  Http404
from django.core.validators import RegexValidator


"""
Legacy code
class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = '__all__'
"""

def validate_insurance(value):
    if value[0].isalpha():
        if len(value) == 12:
            for i in range(1,len(value)):
                if value[i].isalpha():
                    raise ValidationError('Insurance number must start with a letter and be followed by 11 numbers')
        else:
            raise ValidationError('Insurance number must be 12 characters long and begin with a letter.')
    else:
        raise ValidationError('Insurance number must be 12 characters long and begin with a letter.')


def validate_phone(value):
    if len(value) < 10 or len(value) > 10:
        raise ValidationError("Phone numbers must be 10 digits long")
    else:
        for i in value:
            if i.isalpha():
                raise ValidationError("Phone numbers must only contain digits!")

class PatientForm(UserCreationForm):
    username = forms.EmailField(required = True, widget=forms.TextInput(attrs={
        'placeholder' : 'jsmith@website.com',
        'name' : 'username',
        'size' : '50'
    }))
    firstName = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder' : 'John',
        'size' : '50'
    }))
    middleName = forms.CharField(required=False)
    lastName = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder' : 'Smith',
        'size' : '50'
    }))
    suffix = forms.CharField(required=False)
    phoneNumber = forms.CharField(required=False)
    dateOfBirth = forms.DateField(required=False, widget=SelectDateWidget(years=range(1920,2016)))
    addressLine1 = forms.CharField(required=False)
    addressLine2 = forms.CharField(required=False)
    city = forms.CharField(required=False)
    stateProv = forms.CharField(required=False)
    zipCode = forms.CharField(required=False)
    height = forms.CharField(required=False)
    weight = forms.CharField(required=False)

    gender = forms.ChoiceField(choices=(('Male', 'Male'),
                                     ('Female', 'Female'),
                                     ('Other', 'Other'),), required=False,widget=forms.Select())
    hospital = forms.ModelChoiceField(queryset=Hospital.objects.all(), required=True,
                                      widget=forms.Select(), empty_label='None')
    emergency_first = forms.CharField(required=False)
    emergency_last = forms.CharField(required=False)
    emergency_phone = forms.CharField(required=False)
    insurance_num = forms.CharField(required=True, validators=[validate_insurance], widget=forms.TextInput(attrs={
        'placeholder' : 'A01234567890',
        'size' : '50'}))
    insurance_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder' : 'Company Name',
        'size':'50'}))
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), required=False, widget=forms.Select(), empty_label='None')

    class Meta:
        model = User
        fields = ('username', 'email')

    def save(self, commit=True):
        user = super(PatientForm, self).save(commit=False)
        user.username = (self.cleaned_data['username']).lower()
        user.email = (self.cleaned_data['username']).lower()
        user.first_name = self.cleaned_data['firstName']
        user.last_name = self.cleaned_data['lastName']
        user.is_active = True


        if commit:
            user.save()
            g, created = Group.objects.get_or_create(name='Patient')
            g.user_set.add(user)
            patient = Patient.objects.create(theUser=user)
            patient.addressLine1 = self.cleaned_data['addressLine1']
            patient.addressLine2 = self.cleaned_data['addressLine2']
            patient.middleName = self.cleaned_data['middleName']
            patient.hospital = self.cleaned_data['hospital']
            patient.suffix = self.cleaned_data['suffix']
            patient.middleName = self.cleaned_data['middleName']
            patient.phoneNumber = self.cleaned_data['phoneNumber']
            patient.dateOfBirth = self.cleaned_data['dateOfBirth']
            patient.height = self.cleaned_data['height']
            patient.weight = self.cleaned_data['weight']
            patient.gender = self.cleaned_data['gender']

            patient.city = self.cleaned_data['city']
            patient.stateProv = self.cleaned_data['stateProv']
            patient.zipCode = self.cleaned_data['zipCode']
            patient.emergency_first = self.cleaned_data['emergency_first']
            patient.emergency_last = self.cleaned_data['emergency_last']
            patient.emergency_phone = self.cleaned_data['emergency_phone']
            patient.insurance_num = self.cleaned_data['insurance_num']
            patient.insurance_name = self.cleaned_data['insurance_name']
            patient.doctor = self.cleaned_data['doctor']
            patient.save()

            # CREATE NEW LOG ENTRY
            Entry.objects.new_entry(user, 'New user: %s, created, type: Patient' % user.username, datetime.datetime.now())
        return user


class NurseForm(UserCreationForm):

    username = forms.EmailField(required = True, widget=forms.TextInput(attrs={
        'placeholder' : 'jsmith@website.com',
        'name' : 'username',
        'size' : '50'
    }))

    firstName = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder' : 'John',
        'size' : '50'
    }))
    middleName = forms.CharField(required=False)
    lastName = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder' : 'Smith',
        'size' : '50'
    }))

    hospital = forms.ModelChoiceField(queryset=Hospital.objects.all(), required=True, widget=forms.Select(), empty_label='None')

    emergency_first = forms.CharField(required=False)
    emergency_last = forms.CharField(required=False)
    emergency_phone = forms.CharField(required=False)
    phoneNumber = forms.CharField(required=False)



    class Meta:
        model = User
        fields = ('username', 'email')


    def save(self, commit=True):
        user = super(NurseForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['username']
        user.first_name = self.cleaned_data['firstName']
        user.last_name = self.cleaned_data['lastName']
        user.is_active = True


        if commit:
            user.save()
            g, created = Group.objects.get_or_create(name='Nurse')
            g.user_set.add(user)
            nurse = Nurse.objects.create(theUser=user)
            nurse.middleName = self.cleaned_data['middleName']
            nurse.phoneNumber = self.cleaned_data['phoneNumber']
            nurse.emergency_first = self.cleaned_data['emergency_first']
            nurse.emergency_last = self.cleaned_data['emergency_last']
            nurse.emergency_phone = self.cleaned_data['emergency_phone']
            nurse.hospital = self.cleaned_data['hospital']
            nurse.save()

            # CREATE NEW LOG ENTRY
            Entry.objects.new_entry(user, 'New user: %s, created, type: Nurse' % user.username, datetime.datetime.now())

class DoctorForm(UserCreationForm):

    username = forms.EmailField(required = True, widget=forms.TextInput(attrs={
        'placeholder' : 'jsmith@website.com',
        'name' : 'username',
        'size' : '50'
    }))

    firstName = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder' : 'John',
        'size' : '50'
    }))
    middleName = forms.CharField(required=False)
    lastName = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder' : 'Smith',
        'size' : '50'
    }))

    emergency_first = forms.CharField(required=False)
    emergency_last = forms.CharField(required=False)
    emergency_phone = forms.CharField(required=False)
    phoneNumber = forms.CharField(required=False)
    hospital = forms.ModelMultipleChoiceField(queryset=Hospital.objects.all(), required=True,
                                      widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = User
        fields = ('username', 'email')


    def save(self, commit=True):
        user = super(DoctorForm, self).save(commit=False)
        user.username = self.cleaned_data['username'].lower()
        user.email = self.cleaned_data['username'].lower()
        user.first_name = self.cleaned_data['firstName']
        user.last_name = self.cleaned_data['lastName']
        user.is_active = True


        if commit:
            user.save()
            g, created = Group.objects.get_or_create(name='Doctor')
            g.user_set.add(user)
            doctor = Doctor.objects.create(theUser=user)
            doctor.middleName = self.cleaned_data['middleName']
            doctor.phoneNumber = self.cleaned_data['phoneNumber']
            doctor.emergency_first = self.cleaned_data['emergency_first']
            doctor.emergency_last = self.cleaned_data['emergency_last']
            doctor.emergency_phone = self.cleaned_data['emergency_phone']


            doctor.hospital = self.cleaned_data['hospital']
            doctor.save()

            # CREATE NEW LOG ENTRY
            Entry.objects.new_entry(user, 'New user: %s, created, type: Doctor' % user.username, datetime.datetime.now())


class AdminForm(UserCreationForm):

    username = forms.EmailField(required = True, widget=forms.TextInput(attrs={
        'placeholder' : 'jsmith@website.com',
        'name' : 'username',
        'size' : '50'
    }))
    firstName = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder' : 'John',
        'size' : '50'
    }))
    lastName = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder' : 'Smith',
        'size' : '50'
    }))

    class Meta:
        model = User
        fields = ('username', 'email')


    def save(self, commit=True):
        user = super(AdminForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['username']
        user.first_name = self.cleaned_data['firstName']
        user.last_name = self.cleaned_data['lastName']
        user.is_active = True

        if commit:
            user.save()
            g, created = Group.objects.get_or_create(name='Admin')
            g.user_set.add(user)
            admin = Admin.objects.create(theUser=user)
            admin.save()

            # CREATE NEW LOG ENTRY
            Entry.objects.new_entry(user, 'New user: %s, created, type: Admin' % user.username, datetime.datetime.now())




class HospitalForm(forms.Form):


    name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder' : 'Mercy Hospital',
        'size' : '50'
    }))
    address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder' : '1 Main Street',
        'size' : '50'
    }))

    class Meta:
        model = Hospital
        fields = {'name', 'address'}

    def save(self, commit=True):
        if commit:
            hospital = Hospital.objects.create()
            hospital.name = self.cleaned_data['name']
            hospital.address = self.cleaned_data['address']
            hospital.save()


class EditPatientForm(UserChangeForm):
    def validate_height(value):
        for i in range(0,len(value)):
                if value[i].isalpha():
                    raise ValidationError("Must only contain numbers")

    email = forms.EmailField(required=True)
    firstName = forms.CharField(required=True)
    middleName = forms.CharField(required=False)
    lastName = forms.CharField(required=True)
    suffix = forms.CharField(required=False)
    phoneNumber = forms.CharField(required=False, validators=[validate_phone])
    dateOfBirth = forms.DateField(required=False, widget=SelectDateWidget(years=range(1920,2016)))
    addressLine1 = forms.CharField(required=False)
    addressLine2 = forms.CharField(required=False)
    city = forms.CharField(required=False)
    stateProv = forms.CharField(required=False)
    zipCode = forms.CharField(required=False)
    height = forms.CharField(required=False, validators=[validate_height])
    weight = forms.CharField(required=False, validators=[validate_height])
    gender = forms.ChoiceField(choices=(('Male', 'Male'),
                                     ('Female', 'Female'),
                                     ('Other', 'Other'),), required=False,widget=forms.Select())
    hospital = forms.ModelChoiceField(queryset=Hospital.objects.all(), required=True, widget=forms.Select(), empty_label='none')
    emergency_first = forms.CharField(required=False)
    emergency_last = forms.CharField(required=False)
    emergency_phone = forms.CharField(validators=[validate_phone], required=False)
    insurance_num = forms.CharField(required=True, validators=[validate_insurance], widget=forms.TextInput(attrs={
        'placeholder' : 'A01234567890',
        'size' : '50'}))
    insurance_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder' : 'Company Name',
        'size':'50'}))


    def __init__(self, *args, **kwargs):
        self.editor = kwargs.pop('editor', None)

        super(EditPatientForm, self).__init__( *args, **kwargs)


    class Meta:
        model = User
        fields = ('email',)

    def clean_password(self):
        return self.cleaned_data['password']

    def save(self, commit=True):
        user = super(EditPatientForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['firstName']
        user.last_name = self.cleaned_data['lastName']
        user.is_active = True

        if commit:
            user.save()
            if Group.objects.get(name="Patient") in user.groups.all():
                patient = get_user_type(user)

                patient.addressLine1 = self.cleaned_data['addressLine1']
                patient.addressLine2 = self.cleaned_data['addressLine2']
                patient.middleName = self.cleaned_data['middleName']
                patient.hospital = self.cleaned_data['hospital']
                patient.suffix = self.cleaned_data['suffix']
                patient.middleName = self.cleaned_data['middleName']
                patient.phoneNumber = self.cleaned_data['phoneNumber']
                patient.dateOfBirth = self.cleaned_data['dateOfBirth']

                patient.height = self.cleaned_data['height']

                patient.weight = self.cleaned_data['weight']
                patient.gender = self.cleaned_data['gender']

                patient.city = self.cleaned_data['city']
                patient.stateProv = self.cleaned_data['stateProv']
                patient.zipCode = self.cleaned_data['zipCode']
                patient.emergency_first = self.cleaned_data['emergency_first']
                patient.emergency_last = self.cleaned_data['emergency_last']
                patient.emergency_phone = self.cleaned_data['emergency_phone']
                patient.insurance_num = self.cleaned_data['insurance_num']
                patient.insurance_name = self.cleaned_data['insurance_name']


                patient.save()
                # CREATE NEW LOG ENTRY
                Entry.objects.new_entry(user, 'User Profile: %s, edited' % user.username, datetime.datetime.now())

        return user

class EditDoctorForm(UserChangeForm):
    email = forms.EmailField(required=True)
    firstName = forms.CharField(required=True)
    lastName = forms.CharField(required=True)

    emergency_first = forms.CharField(required=False)
    emergency_last = forms.CharField(required=False)
    emergency_phone = forms.CharField(validators=[validate_phone], required=False)
    def __init__(self, *args, **kwargs):
        self.editor = kwargs.pop('editor', None)

        super(EditDoctorForm, self).__init__( *args, **kwargs)


    class Meta:
        model = User
        fields = ('email',)

    def clean_password(self):
        return self.cleaned_data['password']

    def save(self, commit=True):
        user = super(EditDoctorForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['firstName']
        user.last_name = self.cleaned_data['lastName']
        user.is_active = True

        if commit:
            user.save()
            if Group.objects.get(name="Doctor") in user.groups.all():
                doctor = get_user_type(user)

                doctor.emergency_first = self.cleaned_data['emergency_first']
                doctor.emergency_last = self.cleaned_data['emergency_last']
                doctor.emergency_phone = self.cleaned_data['emergency_phone']
                doctor.save()
                # CREATE NEW LOG ENTRY
                Entry.objects.new_entry(user, 'User Profile: %s, edited' % user.username, datetime.datetime.now())


            elif Group.objects.get(name="Nurse") in user.groups.all():
                nurse = get_user_type(user)

                nurse.emergency_first = self.cleaned_data['emergency_first']
                nurse.emergency_last = self.cleaned_data['emergency_last']
                nurse.emergency_phone = self.cleaned_data['emergency_phone']
                nurse.save()
                # CREATE NEW LOG ENTRY
                Entry.objects.new_entry(user, 'User Profile: %s, edited' % user.username, datetime.datetime.now())


        return user

class EditAdminForm(UserChangeForm):
    email = forms.EmailField(required=True)
    firstName = forms.CharField(required=True)
    lastName = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        self.editor = kwargs.pop('editor', None)

        super(EditAdminForm, self).__init__( *args, **kwargs)


    class Meta:
        model = User
        fields = ('email',)

    def clean_password(self):
        return self.cleaned_data['password']

    def save(self, commit=True):
        user = super(EditAdminForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['firstName']
        user.last_name = self.cleaned_data['lastName']
        user.is_active = True

        if commit:
            user.save()
            if Group.objects.get(name="Admin") in user.groups.all():
                # CREATE NEW LOG ENTRY
                Entry.objects.new_entry(user, 'User Profile: %s, edited' % user.username, datetime.datetime.now())


        return user

def get_hospitals():
        return Hospital.objects.all()


def get_user_type(user):
    if Group.objects.get(name='Patient') in user.groups.all():

        patient = None
        for patientIt in Patient.objects.all():
            if patientIt.theUser == user:
                patient = patientIt
        return patient

    elif Group.objects.get(name='Doctor') in user.groups.all():

        doctor = None
        for doctorIt in Doctor.objects.all():
            if doctorIt.theUser == user:
                doctor = doctorIt
        return doctor

    elif Group.objects.get(name='Nurse') in user.groups.all():
        nurse = None
        for nurseIt in Nurse.objects.all():
            if nurseIt.theUser == user:
                nurse = nurseIt
        return nurse
        #return Nurse.objects.filter(user=user)[0]
    elif Group.objects.get(name='Admin') in user.groups.all():
        admin = None
        for adminIt in Admin.objects.all():
            if adminIt.theUser == user:
                admin = adminIt
        return admin
    else:
        return user

