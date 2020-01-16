from django.db import models
from django.conf import settings
# Create your models here.


class Equipment(models.Model):
    lab_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    marker = models.CharField(max_length=100)
    date_supplied = models.DateTimeField(blank=True, null=True)
    location_in_lab = models.CharField(max_length=130)
    date_serviced = models.DateTimeField(
        blank=True, null=True)
    next_service_date = models.DateTimeField(
        blank=True, null=True)
    date_caliberated = models.DateTimeField(
        blank=True, null=True)
    next_caliberation_date = models.DateTimeField(
        blank=True, null=True)
    company_that_serviced = models.CharField(max_length=130)
    company_that_caliberated = models.CharField(max_length=130)
    price = models.FloatField(default=0.000)
    data_entry_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        default=1,
        null=True,
        blank=True
    )
    using_personel = models.CharField(max_length=130)
    project = models.CharField(max_length=130)

    def __str__(self):
        return f"{self.name}"
