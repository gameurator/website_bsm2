from django.db import models


class ControllerType(models.Model):
    category = models.CharField(max_length=50, unique=True, verbose_name="Category")

    def __str__(self):
        return self.category


class EnergyName(models.Model):
    name = models.CharField(verbose_name="Energy Name", unique=True, max_length=50)
    category = models.ForeignKey('ControllerType', verbose_name="Category", on_delete='PROTECT')

    def __str__(self):
        return self.name


class SubDevice(models.Model):
    device_id = models.IntegerField(default=0, unique=True, verbose_name='Device Id')
    device_name = models.ForeignKey('Device', verbose_name='Device Name', on_delete='PROTECT')
    energy_names = models.ManyToManyField('EnergyName', verbose_name='Energy Name')
    category = models.ForeignKey('ControllerType', on_delete='PROTECT', verbose_name='Category')

    def __str__(self):
        return self.device_name + self.category


class Device(models.Model):
    # device_id = models.IntegerField(default=0, unique=True, verbose_name="device_id")
    device_name = models.CharField(max_length=12, unique=True, verbose_name="device_name")

    # energy_names = models.ManyToManyField('EnergyName', verbose_name='Energy Name')
    # category = models.ForeignKey('ControllerType', verbose_name="Category", on_delete='PROTECT')

    def __str__(self):
        return self.device_name
#t