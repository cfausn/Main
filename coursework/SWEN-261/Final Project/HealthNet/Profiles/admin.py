from django.contrib import admin

from .models import *

admin.site.register(Patient)

admin.site.register(Doctor)

admin.site.register(Nurse)

admin.site.register(Hospital)

admin.site.register(Admin)

admin.site.register(Surgery)

admin.site.register(Prescription)

admin.site.register(TestResults)

# Register your models here.
