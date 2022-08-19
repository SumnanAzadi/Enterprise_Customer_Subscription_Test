from rest_framework import serializers

from employee.serializers import PhoneSerializers
from .models import Company, Plan


class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class PlanSerializers(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'


class CompanyPhoneSerializers(serializers.ModelSerializer):
    phones = PhoneSerializers(many=True, read_only=True, source='company')

    class Meta:
        model = Company
        fields = ('name', 'phones')
