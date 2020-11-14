from django.contrib import admin

# Register your models here.

from .models import Clientes, Vehiculo, Estado, Proveedor, Fotos

# Register your models here.

class VehiculoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Clientes)
admin.site.register(Vehiculo, VehiculoAdmin)
admin.site.register(Estado)
admin.site.register(Proveedor)
admin.site.register(Fotos)
