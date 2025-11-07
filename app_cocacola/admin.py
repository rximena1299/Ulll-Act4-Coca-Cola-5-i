from django.contrib import admin
from .models import Cliente, Proveedor

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'telefono', 'email', 'fecha_registro')
    search_fields = ('nombre', 'apellido', 'email', 'telefono')

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_empresa', 'contacto', 'telefono', 'correo', 'pais')
    search_fields = ('nombre_empresa', 'contacto', 'correo', 'telefono')
