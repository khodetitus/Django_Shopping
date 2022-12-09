from django.contrib import admin
from .models import Customer, Profile, Address, OtpCode
from core.admin import BaseAdmin

# Register your models here.

admin.site.register(Customer)
admin.site.register(Profile)
admin.site.register(Address)
admin.site.register(OtpCode)
