from rest_framework import serializers
from .models import Company, Plan


class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class PlanSerializers(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'
