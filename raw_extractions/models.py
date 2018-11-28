from django.db import models
from django.utils import timezone
from api_management.api_calls import call_SLV_getDevicesLogValues, historize_log_values
from settings import SLV_URL, logi, FILE_PATH_FIELD


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
    device_value_history = models.FilePathField(path=FILE_PATH_FIELD + device_name.device_str + device_id.__str__(),
                                                verbose_name="Value_storage_file")

    def __str__(self):
        return self.device_name.device_str + self.category.category

    def update_log_values(self):
        """
        updates the file containing all log values of SubDevice
        :return: None
        """
        result = call_SLV_getDevicesLogValues(SLV_URL, logi, 'json', self.device_id,
                                     self.energy_names.all().values_list('name', flat=True),
                                     (timezone.now() - timezone.timedelta(days=15)).strftime("%d/%m/%Y %H:%M:%S"),
                                     timezone.now().strftime("%d/%m/%Y %H:%M:%S"),
                                     self.device_value_history)
        historize_log_values(self.device_value_history, result.json())


class Device(models.Model):
    # device_id = models.IntegerField(default=0, unique=True, verbose_name="device_id")
    device_str = models.CharField(max_length=12, unique=True, verbose_name="device_str")
    device_name = models.CharField(max_length=100, unique=True, verbose_name="device_name")
    device_group = models.CharField(max_length=50, verbose_name="device_group")

    # energy_names = models.ManyToManyField('EnergyName', verbose_name='Energy Name')
    # category = models.ForeignKey('ControllerType', verbose_name="Category", on_delete='PROTECT')

    def __str__(self):
        return self.device_name
#t