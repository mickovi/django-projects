from django.contrib import admin
from . models import Service

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

# Registramos el servicio y su configuración
admin.site.register(Service, ServiceAdmin)