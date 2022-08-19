from django.contrib import admin

from employee.models import Employee, Phone

admin.site.register(Phone)
admin.site.register(Employee)