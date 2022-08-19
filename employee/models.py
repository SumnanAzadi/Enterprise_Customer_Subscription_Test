from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

from company.models import Company, Plan


class Employee(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Phone(models.Model):
    phone = PhoneNumberField(region="BD", unique=True)
    company = models.ForeignKey(Company, related_name='company', on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, related_name='employee', on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, related_name='plan', on_delete=models.CASCADE, null=True)
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return str(self.phone) + '-' + str(self.company.name) + '-' + str(self.employee.name) + '- Primary: ' + str(self.is_primary)
