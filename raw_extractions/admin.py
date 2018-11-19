from django.contrib import admin
from .models import Device


# Register your models here.

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'name', 'energy_names')
    list_filter = ('name', 'energy_names',)
    # date_hierarchy = 'date'
    ordering = ('name',)
    search_fields = ('name', 'energy_names')


admin.site.register(Device)
