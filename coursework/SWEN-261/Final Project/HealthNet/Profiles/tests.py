import datetime

from django.test import TestCase
from django.core.urlresolvers import reverse

from django.db import models

from .models import *
from Schedule.models import *



def createUser():
    u = User
    u.firstName = "first"
    u.lastName = "last"
    u.middleName = "middle"
    u.suffix = "m"
    u.dateOfBirth = "dob"
    u.gender = "g"
    u.phoneNumber = "212"
    u.username = "name"
    u.password = "pass"

    u.addressLine1 = "1"
    u.addressLine2 = "2"
    u.city = "city"
    u.stateProv = "st"
    u.zipCode = "11111"
    u.hospitals = "h"

    return u

def createDoctor():
    u = User.objects.create(username = "Doctor")
    d = Doctor.objects.create(max_patients = 3, theUser = u)

    d.save()
    return u

def createPatient():
    u = User.objects.create(username = "Patient")
    p = Patient.objects.create(theUser = u)

    p.appointment = []
    p.prescription = []

    return u

def createNurse():
    u = User.objects.create(username = "Nurse")
    n = Nurse.objects.create(theUser = u)

    return u

def createAdmin():
    u = User.objects.create(username = "Admin")
    a = Admin.objects.create(theUser = u)

    return u

class UserTestCase(TestCase):
    def testNames(self):
        u = createUser()
        self.assertEqual(u.firstName, "first")
        self.assertEqual(u.middleName, "middle")
        self.assertEqual(u.lastName, "last")
        self.assertEqual(u.username, "name")


class DoctorTestCase(TestCase):
    def testDoctor(self):
        u = User.objects.create(username = "Doctor")
        d = Doctor.objects.create(max_patients = 3, theUser = u)

        self.assertEqual(3, d.max_patients)

class NurseTestCase(TestCase):
    def testScheduleAppointment(self):
        n = createNurse()
        d = createDoctor()
        p = createPatient()


class ViewsTestCase(TestCase):
    def testIndex(self):
        resp = self.client.get('/Profiles/')
        self.assertEqual(resp.status_code, 302)

    def test404page(self):
        resp = self.client.get('/wqdsfgb/profile')
        self.assertEqual(resp.status_code, 200)


class PermissionsTestCase(TestCase):

    def testUserIsNurse(self):
        n = createNurse()
        self.assertTrue(userIsNurse(n))

    def testUserIsPatient(self):
        p = createPatient()
        self.assertTrue(userIsPatient(p))

    def testUserIsAdmin(self):
        a = createAdmin()
        self.assertTrue(userIsAdmin(a))

    def testUserIsDoctor(self):
        d = createDoctor()
        self.assertTrue(userIsDoctor(d))

class DoctorAvailabilityTestCase(TestCase):
    def setUp(self):
        u = User.objects.create(username = "Doctor")
        d = Doctor.objects.create(max_patients = 3, theUser = u)
        p1 = Patient.objects.create(doctor = d)
        p2 = Patient.objects.create(doctor = d)
        p3 = Patient.objects.create(doctor = d)

    def test_doctor_available_at_max(self):
        d = Doctor.objects.get(username ="Doctor")
        self.assertEqual(getDoctorIsAvailable(d), False)

class PrescriptionsTestCase(TestCase):
    def testPrescriptions(self):
        p = Prescription.createPrescription(self, "patient", "name", 3, "e")
        self.assertEqual(p.name, "name")