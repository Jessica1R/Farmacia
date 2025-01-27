# models.py
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    cantidad = models.IntegerField()

    def actualizar_cantidad(self, cantidad):
        self.cantidad += cantidad
        self.save()

class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()

    def verificar_stock(self, producto_id):
        stock = Stock.objects.filter(sucursal=self, producto_id=producto_id).first()
        return stock and stock.cantidad > 0

    def actualizar_stock(self, producto_id, cantidad):
        stock, created = Stock.objects.get_or_create(sucursal=self, producto_id=producto_id)
        stock.cantidad += cantidad
        stock.save()

    def transferir_producto(self, producto_id, cantidad, sucursal_destino):
        stock_origen = Stock.objects.filter(sucursal=self, producto_id=producto_id).first()
        if stock_origen and stock_origen.cantidad >= cantidad:
            stock_origen.cantidad -= cantidad
            stock_origen.save()
            sucursal_destino.actualizar_stock(producto_id, cantidad)

class Stock(models.Model):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()

class EstadoEntrega(models.TextChoices):
    PENDIENTE = 'Pendiente', 'Pendiente'
    ENTREGADO = 'Entregado', 'Entregado'

class Pedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    sucursal_origen = models.ForeignKey(Sucursal, related_name='pedidos_origen', on_delete=models.CASCADE)
    sucursal_destino = models.ForeignKey(Sucursal, related_name='pedidos_destino', on_delete=models.CASCADE)
    estado = models.CharField(
        max_length=10,
        choices=EstadoEntrega.choices,
        default=EstadoEntrega.PENDIENTE
    )

    def actualizar_estado(self, estado):
        self.estado = estado
        self.save()
