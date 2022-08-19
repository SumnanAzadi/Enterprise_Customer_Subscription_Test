from django.shortcuts import render
from rest_framework import viewsets
from employee.models import Employee, Phone
from employee.serializers import EmployeeSerializers, PhoneSerializers


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializers

