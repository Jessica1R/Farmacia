from django.db import models

class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    inventario = models.TextField()  # Asumo que inventario es una lista serializada.

    def verificar_stock(self, productoid, cantidad):
        # Lógica para verificar stock.
        pass

    def actualizar_stock(self, productoid, cantidad):
        # Lógica para actualizar stock.
        pass

    def transferir_producto(self, productoid, cantidad, sucursal_destino):
        # Lógica para transferir producto entre sucursales.
        pass

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    cantidad = models.IntegerField()

    def actualizar_cantidad(self, cantidad):
        self.cantidad += cantidad
        self.save()

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class EstadoEntrega(models.TextChoices):
    PENDIENTE = 'Pendiente', 'Pendiente'
    ENTREGADO = 'Entregado', 'Entregado'


class Pedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='pedidos')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    sucursal_origen = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name='pedidos_origen')
    sucursal_destino = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name='pedidos_destino')
    estado = models.CharField(max_length=10, choices=EstadoEntrega.choices, default=EstadoEntrega.PENDIENTE)

    def actualizar_estado(self, estado):
        self.estado = estado
        self.save()

    def __str__(self):
        return f"Pedido {self.id} - {self.producto.nombre}"


class Stock(models.Model):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name='stock')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='stock')
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.cantidad} - {self.producto.nombre} en {self.sucursal.nombre}"


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=50)

    def autenticar(self):
        # Lógica de autenticación
        pass

    def __str__(self):
        return self.nombre
