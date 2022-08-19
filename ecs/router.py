from rest_framework import routers
from company.views import CompanyViewSet, PlanViewSet, CompanyPhoneViewSet
from employee.views import PhoneViewSet, EmployeeViewSet

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='company')
router.register(r'plans', PlanViewSet, basename='plans')
router.register(r'phones', PhoneViewSet, basename='phones')
router.register(r'employees', EmployeeViewSet, basename='employees')
router.register(r'company_phones', CompanyPhoneViewSet, basename='company_phones')
