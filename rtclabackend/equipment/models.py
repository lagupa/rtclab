from django.db import models

# Create your models here.


class Equipment(models.Model):
    lab_id = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=30)
    marker = models.CharField(max_length=20)
    data_supplied = models.DateTimeField(blank=True, null=True)
    location_in_lab = models.CharField(max_length=30)
    date_serviced = models.DateTimeField(blank=True, null=True)
    next_service_date = models.DateTimeField(blank=True, null=True)
    date_caliberated = models.DateTimeField(blank=True, null=True)
    next_caliberation_date = models.DateTimeField(blank=True, null=True)
    company_that_serviced = models.CharField(max_length=30)
    company_that_caliberated = models.CharField(max_length=30)
    using_personel = models.CharField(max_length=30)
    project = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"
