from django.db import models


# Create your models here.
class Device(models.Model):
    device_id = models.IntegerField(default=0, unique=True, verbose_name="device_id")
    device_name = models.CharField(max_length=12, unique=True, verbose_name="device_name")
    energy_names = models.ForeignKey('EnergyNames', verbose_name='Energy Names')
    category = models.ManyToManyField('ControllerType', verbose_name="Category")


class ControllerType(models.Model):
    category = models.CharField(max_length=50, unique=True, verbose_name="Category")


class EnergyNames(models.Model):
    name = models.CharField(unique=True, verbose_name="Energy Name")
    category = models.ManyToManyField('ControllerType', verbose_name="Category")
