from django.db import models
from django.conf import settings
# Create your models here.


class Reagent(models.Model):
    lab_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    CAT_number = models.IntegerField()
    batch_number = models.IntegerField()
    quantity = models.IntegerField()
    marker = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    date_supplied = models.DateTimeField(blank=True, null=True)
    manufacturer_date = models.DateTimeField(blank=True, null=True)
    expiry_date = models.DateTimeField(blank=True, null=True)
    storage_requirement = models.TextField()
    location_in_lab = models.CharField(max_length=130)
    ordered_by = models.CharField(max_length=130)
    project_code = models.CharField(max_length=130)
    data_entry_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        default=1,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.name}"
