from django.contrib import admin
from .models import Producto, Sucursal, Stock, Cliente, Pedido

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'cantidad')
    search_fields = ('nombre',)

class SucursalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion')
    search_fields = ('nombre', 'direccion')

class StockAdmin(admin.ModelAdmin):
    list_display = ('sucursal', 'producto', 'cantidad')
    list_filter = ('sucursal', 'producto')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion')
    search_fields = ('nombre',)

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cliente', 'sucursal_origen', 'sucursal_destino', 'estado')
    list_filter = ('estado', 'sucursal_origen', 'sucursal_destino')
    search_fields = ('producto__nombre', 'cliente__nombre')

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Sucursal, SucursalAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Pedido, PedidoAdmin)
