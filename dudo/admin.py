from django.contrib import admin
from .models import *


class DeviceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    prepopulated_fields = {
        "slug": ('title',)
    }
admin.site.register(Device, DeviceAdmin)