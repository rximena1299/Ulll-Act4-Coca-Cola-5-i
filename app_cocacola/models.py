from django.db import models

# ==========================================
# MODELO: CLIENTE
# ==========================================
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    fecha_registro = models.DateField(auto_now_add=True)
    preferencia = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ==========================================
# (PROVEEDOR y PRODUCTO quedan pendientes - abajo hay plantillas comentadas)

class Proveedor(models.Model):
    nombre_empresa = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(max_length=100)
    direccion = models.CharField(max_length=200)
    pais = models.CharField(max_length=50)
    tipo_producto_suministro = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_empresa
"""
class Producto(models.Model):
    nombre_producto = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    stock_actual = models.IntegerField()
    fecha_fabricacion = models.DateField()
    fecha_vencimiento = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_producto
"""