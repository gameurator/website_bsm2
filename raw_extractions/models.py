from django.db import models


# Create your models here.
class Device(models.Model):
    device_id = models.IntegerField(default=0, unique=True,verbose_name="device_id")
    device_name = models.CharField(max_length=12, unique=True, verbose_name="device_name")
    energy_names = models.ExpressionList('TotalKWHPositive')
