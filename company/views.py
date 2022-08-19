from django.shortcuts import render
from rest_framework import viewsets
from company.models import Company, Plan
from company.serializers import CompanySerializers, PlanSerializers, CompanyPhoneSerializers


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializers


class CompanyPhoneViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'options', 'head']
    queryset = Company.objects.all()
    serializer_class = CompanyPhoneSerializers
