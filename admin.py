from django.contrib import admin
from .models import Producto, Sucursal, Stock, Cliente, EstadoEntrega, Pedido


# Registro del modelo Producto
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'cantidad')
    search_fields = ('nombre',)
    list_filter = ('precio',)
    ordering = ('nombre',)


# Registro del modelo Sucursal
@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion')
    search_fields = ('nombre', 'direccion')
    ordering = ('nombre',)


# Registro del modelo Stock
@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('sucursal', 'producto', 'cantidad')
    list_filter = ('sucursal', 'producto')
    search_fields = ('sucursal_nombre', 'producto_nombre')
    autocomplete_fields = ('sucursal', 'producto')


# Registro del modelo Cliente
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion')
    search_fields = ('nombre', 'direccion')
    ordering = ('nombre',)


# Registro del modelo EstadoEntrega
@admin.register(EstadoEntrega)
class EstadoEntregaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    ordering = ('nombre',)

# Registro del modelo Pedido
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = (
        'producto', 'cliente', 'sucursal_origen', 'sucursal_destino', 'estado')
    list_filter = ('estado', 'sucursal_origen', 'sucursal_destino')
    search_fields = ('producto_nombre', 'clientenombre', 'sucursal_origen_nombre',
                     'sucursal_destino__nombre')
    list_editable = ('estado',)
    autocomplete_fields = (
        'producto', 'cliente', 'sucursal_origen', 'sucursal_destino')
    ordering = ('estado', 'cliente')
    