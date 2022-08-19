from rest_framework import serializers

from employee.models import Employee, Phone


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class PhoneSerializers(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'
