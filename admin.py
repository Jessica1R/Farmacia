from django.contrib import admin
# admin.py
# Importación de modelos
from django.contrib import admin
from .models import Producto, Sucursal, Stock, Cliente, Pedido, Usuario

# Registro de modelos
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'cantidad')
    search_fields = ('nombre',)

class SucursalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion')
    search_fields = ('nombre',)

class StockAdmin(admin.ModelAdmin):
    list_display = ('sucursal', 'producto', 'cantidad')
    search_fields = ('sucursal__nombre', 'producto__nombre')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion')
    search_fields = ('nombre',)

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'producto', 'cliente', 'sucursal_origen', 'sucursal_destino', 'estado')
    list_filter = ('estado',)
    search_fields = ('producto__nombre', 'cliente__nombre')

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rol')
    search_fields = ('nombre', 'rol')

# Register your models here.
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Sucursal, SucursalAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Usuario, UsuarioAdmin)
