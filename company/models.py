from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Plan(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    PLANS_VALIDITY = [
        ('', 'No contract'),
        ('12', '12 Months'),
    ]
    validity = models.CharField(max_length=25, choices=PLANS_VALIDITY, null=True, blank=True)

    def __str__(self):
        return self.name + '-' + str(self.price) + '-' + str(self.get_validity_display())
