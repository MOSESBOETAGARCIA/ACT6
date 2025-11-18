from django.db import models

# ==========================================
# MODELO: CLIENTE
# ==========================================
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    fecha_ingreso = models.DateField()
    domicilio = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ==========================================
# MODELO: ORDEN
# ==========================================
class Orden(models.Model):
    id_orden = models.AutoField(primary_key=True)
    fecha_orden = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)
    fecha_pago = models.DateField()
    sucursal = models.CharField(max_length=100)
    id_empleado = models.ForeignKey('Empleado', on_delete=models.CASCADE)
    id_cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)

    def __str__(self):
        return f"Orden {self.id_orden}"

# ==========================================
# MODELO: EMPLEADO
# ==========================================
class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    domicilio = models.TextField()
    fecha_ingreso = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ==========================================
# MODELO: PRODUCTO
# ==========================================
class Producto(models.Model):
    id_productos = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50)
    disponible = models.BooleanField(default=True)
    id_proveedor = models.ForeignKey('Proveedor', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre_producto

# ==========================================
# MODELO: PROVEEDOR
# ==========================================
class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=100, default='Proveedor Desconocido')
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    id_producto = models.ForeignKey('Producto', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre_proveedor
