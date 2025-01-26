# models.py
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    cantidad = models.IntegerField()

    def actualizar_cantidad(self, cantidad):
        self.cantidad = cantidad
        self.save()

class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    inventario = models.ManyToManyField(Producto, through='Stock')

    def verificar_stock(self, producto_id):
        stock = self.stock_set.filter(producto_id=producto_id).first()
        return stock.cantidad > 0 if stock else False

    def actualizar_stock(self, producto_id, cantidad):
        stock = self.stock_set.filter(producto_id=producto_id).first()
        if stock:
            stock.cantidad += cantidad
            stock.save()

    def transferir_producto(self, producto_id, cantidad, sucursal_destino):
        if self.verificar_stock(producto_id):
            self.actualizar_stock(producto_id, -cantidad)
            sucursal_destino.actualizar_stock(producto_id, cantidad)

class Stock(models.Model):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()

class Pedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    sucursal_origen = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name='pedidos_origen')
    sucursal_destino = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name='pedidos_destino')
    estado = models.CharField(max_length=50)

    def actualizar_estado(self, estado):
        self.estado = estado
        self.save()

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=50)

    def autenticar(self):
        # Implementación de autenticación
        pass
from django.db import models

# Create your models here.
