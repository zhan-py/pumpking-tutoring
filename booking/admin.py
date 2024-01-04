from django.contrib import admin
from .models import Subject, Program, Booking

# Register your models here.
admin.site.register(Subject)
admin.site.register(Program)
admin.site.register(Booking)