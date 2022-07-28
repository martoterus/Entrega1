from django.contrib import admin

from Appventas.models import bicicletas, indumentaria, repuestos

# Register your models here.

admin.site.register(bicicletas)
admin.site.register(repuestos)
admin.site.register(indumentaria)
