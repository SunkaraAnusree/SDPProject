from django.contrib import admin

from .models import Admin, Registration, Contactus, RecruiterRegistration, Enroll

admin.site.register(Admin)
admin.site.register(Contactus)
admin.site.register(Registration)
admin.site.register(RecruiterRegistration)
admin.site.register(Enroll)