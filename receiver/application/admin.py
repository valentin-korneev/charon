from django.contrib import admin
from receiver.application.model import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    ordering = ['name']
