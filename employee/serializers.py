from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from employee.models import Employee, Phone


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class PhoneSerializers(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'

    def validate(self, attrs):
        employee = attrs.get('employee')
        is_primary = attrs.get('is_primary')
        company = attrs.get('company')
        plan = attrs.get('plan')

        # If the phone is selected as primary, then make sure that there is only one primary phone for the employee.
        if is_primary:
            is_employee_has_primary_phone = Phone.objects.filter(employee=employee,
                                                                 is_primary=True).values_list('phone',
                                                                                              flat=True)
            if is_employee_has_primary_phone:
                msg = {"Primary_Phone": ["This user has already a primary number. Current primary number is {}".
                                             format(is_employee_has_primary_phone[0])]}
                raise ValidationError(msg)

        # If plan is selected, then make sure that employee has not already a plan in the selected company.
        elif plan:
            is_employee_has_plan_in_company = Phone.objects.filter(employee=employee,
                                                                   company=company,
                                                                   plan__isnull=False)
            employee_current_plan = Phone.objects.filter(employee=employee,
                                                         company=company).values_list('plan__name',
                                                                                      flat=True)
            if is_employee_has_plan_in_company:
                msg = {"Plan": ["This user has already a plan under {} company. Current plan is {}".
                                    format(company, employee_current_plan[0])]}
                raise ValidationError(msg)

        return attrs