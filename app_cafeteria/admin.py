from django.contrib import admin
from .models import Cliente, Empleado, Orden, Producto, Proveedor

admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Orden)
admin.site.register(Producto)
admin.site.register(Proveedor)
