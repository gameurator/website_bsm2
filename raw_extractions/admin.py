from django.contrib import admin
from .models import Device, ControllerType, EnergyName, SubDevice


# Register your models here.

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_name',)
    list_filter = ('device_name',)
    ordering = ('device_name',)
    search_fields = ('device_name',)


class SubDeviceAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'category')
    list_filter = ('device_name', 'category')
    ordering = ('category', 'device_name')
    search_fields = ('device_name', 'category')


class ControllerTypeAdmin(admin.ModelAdmin):
    list_display = ('category',)
    list_filter = ('category',)
    ordering = ('category',)
    search_fields = ('category',)


class EnergyNameAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    ordering = ('name',)
    search_fields = ('name',)


admin.site.register(ControllerType, ControllerTypeAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(EnergyName, EnergyNameAdmin)
admin.site.register(SubDevice, SubDeviceAdmin)
